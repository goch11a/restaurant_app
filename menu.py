#'kitchen management'- ის add new dish და edit dish ფუნქციები არის ეს ორი

import csv
import pandas as pd
from tabulate import tabulate

fields = ['N', 'Dish', 'Price']
fields2 = ['N', 'Dish', 'Ingredient','Unit', 'Quantity']
filename = "menu.csv"
filename2 = "dish_ingredients.csv"
filename3 = "warehouse.csv"
items = []

#print((items[0])['Price'])

def main():
    num = input("num: ")
    if num == "1":
        new_dish()
        calculate_dish_costs()
    elif num == "2":
        edit_dish()
    elif num == "3":
        get_order()
    else:
        delete_dish()
    

#----------------------------------------------------------------------------
def new_dish():
    dish_name = input("Name of dish:  ").strip()
    ingredients = input("Input ingredients(use comma):  ")
    ingr_list = ingredients.split(",")
    for ingredient in ingr_list:
        while True:
            unit = input(f"Unit for {ingredient.strip().title()} per dish (Use only: Kg, L or Piece): ").strip().title()
            if unit in ["Kg", "L", "Piece"]:
                break
        while True:
            try:
                quantity = float(input(f"Quantity for {ingredient.strip().title()} per dish (Only digit!): ").strip())
                break
            except ValueError :
                print("Only digits!")
        
   
        try:
            with open(filename2, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                if rows:
                    last_num = int(rows[-1]['N'])
                else:
                    last_num = 0
        except FileNotFoundError:
            last_num = 0
    
        new_num = last_num +1
    
        mydict = [{'N': new_num, 'Dish': dish_name.title(), 'Ingredient': ingredient.strip().title(), 'Unit': unit, 'Quantity': quantity}]
        
        with open(filename2, 'a', newline= '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields2)
            if last_num == 0:
                writer.writeheader()
            writer.writerows(mydict)
    
    while True:
        try:
            dish_price = float(input("Price of dish: ").strip())
            break
        except ValueError :
            print("Only digits!")
        
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            if rows:
                last_num = int(rows[-1]['N'])
            else:
                last_num = 0
    except FileNotFoundError:
        last_num = 0
    
    new_num = last_num +1
    
    mydict = [{'N': new_num, 'Dish': dish_name.title(), 'Price': dish_price}]
    
    with open(filename, 'a', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if last_num == 0:
            writer.writeheader()
        writer.writerows(mydict)

def calculate_dish_costs():
    ingredients = []
    products = {}

    with open(filename3, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products[row['Product']] = float(row['Unit price'])

    with open(filename2, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ingredients.append(row)

    dishes = []
    for ingredient in ingredients:
        if ingredient['Dish'] not in dishes:
            dishes.append(ingredient['Dish'])

    dish_costs = {}
    for dish in dishes:
        total_cost = 0.0
        for ingredient in ingredients:
            if ingredient['Dish'] == dish:
                product_name = ingredient['Ingredient']
                quantity = float(ingredient['Quantity'])
                if product_name in products:
                    unit_price = products[product_name]
                    total_cost += quantity * unit_price
        dish_costs[dish] = total_cost

    for dish, cost in dish_costs.items():
        print(f"The cost of {dish} is: {cost:.2f}Lari")

    # ამის ქვევით რაცაა ეგ მენიუსთვისაა

#--------------------------------------------------------------------
def edit_dish():
    #items = []
    

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)

    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))

    while True:
        try:
            dish_order = int(input("Choose order of dish, which you want to change: ").strip())
            break
        except ValueError:
            print("Only digits!")
    while True:
        try:
            change_item = input("If you want to change Dish name type D\nIf you want to change Price name type P\n\nType D/P: ").upper()
            if change_item in ["D", "P", "DISH", "PRICE"]:
                break
        except ValueError:
            print("Enter valid input!")

    dish_position = dish_order - 1
    old_dish_name = items[dish_position]['Dish']  # Save the old dish name
    if change_item in ["D", "Dish"]:
        change = "Dish"
        new_dish_value = (input("Enter new value: ").title()).strip()
    else:
        change = "Price"
        while True:
            try:
                new_dish_value = int(input("Enter new value: ").strip())
                break
            except ValueError:
                print("Only digits!")

    df = pd.read_csv(filename)
    df.loc[dish_position, change] = new_dish_value
    df.to_csv(filename, index=False)

    # Update dish name in dish_ingredients.csv using pandas
    if change == "Dish":
        df_ingredients = pd.read_csv(filename2)
        df_ingredients.loc[df_ingredients['Dish'] == old_dish_name, 'Dish'] = new_dish_value
        df_ingredients.to_csv(filename2, index=False)
#--------------------------------------------------------------------------
def delete_dish():
    #ეს შეიძლება ცალკე გავიდეს და ზოგად ცვლადად ჩამოყალიბდეს თაბულეიტამდე
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))

    while True:
        try:
            dish_order = int(input("Choose order of dish, which you want to delete: ").strip())
            break
        except ValueError :
            print("Only digits!")

    dish_name = items[dish_order - 1]['Dish']    
    items.pop(dish_order - 1)

    
    with open(filename, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for n, i in enumerate(items):
            i['N'] = n + 1
            writer.writerow(i)

    
    dish_ingredients = []
    with open(filename2, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Dish'] != dish_name:
                dish_ingredients.append(row)

    with open(filename2, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields2)
        writer.writeheader()
        for n, row in enumerate(dish_ingredients):
            row['N'] = n + 1
            writer.writerow(row)

#-------------------------------------------------------
def get_order():
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))
    

    order_list = []
    order_sum = []

    while True:
        try:
            order_num = int(input("Choose order of dish, which you want to choose: ").strip())
        except ValueError :
            print("Only digits!")
        add_order = input("Do you want something else? Y/N\nAnswer: ").lower()
        if add_order not in ["y","n"]:
            raise ValueError("Enter valid input!")
        elif add_order == "y":
            order = (items[order_num - 1])['Dish']
            order_list.append(order)
            order_price = (items[order_num - 1])['Price']
            order_sum.append(order_price)
            continue
        else:
            order = (items[order_num - 1])['Dish']
            order_list.append(order)
            order_price = (items[order_num - 1])['Price']
            order_sum.append(order_price)
            break
    
    # ეს უნდა დარეთარნდეს, გამოიპრინტოს და ფასები დაჯამდეს
    print(order_list)
    print(order_sum) 

    

main()