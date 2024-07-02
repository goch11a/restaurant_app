import csv
import os
from tabulate import tabulate
from collections import Counter

filename = "menu.csv"
filename2 = "dish_ingredients.csv"
filename3 = "warehouse.csv"
filename4 = "incomes.csv"
items = []

def get_order():
    print("Hello, welcome to Burger Bar Krikina")
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
        except ValueError:
            print("Only digits!")
            continue
        if order_num < 1 or order_num > len(items):
            print("Invalid dish number!")
            continue

        order = (items[order_num - 1])['Dish']
        order_list.append(order)
        order_price = (items[order_num - 1])['Price']
        order_sum.append(float(order_price))
        
        add_order = input("Do you want something else? Y/N\nAnswer: ").lower()
        if add_order == 'n':
            break

    sum_pay = sum(order_sum)
    dish_counts = Counter(order_list)

    table_data = []
    for dish, count in dish_counts.items():
        table_data.append([count, dish])

    table = tabulate(table_data, headers=["Quantity", "Dish"], tablefmt="grid")
    print(table)
    print("Please wait while the order is being processed.")
    return table_data, sum_pay

def get_ingredients(order_list):
    dish_ingredients = {}

    with open(filename2, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dish = row['Dish']
            if dish not in dish_ingredients:
                dish_ingredients[dish] = []
            dish_ingredients[dish].append({
                'Ingredient': row['Ingredient'],
                'Unit': row['Unit'],
                'Quantity': float(row['Quantity'])
            })
    
    required_ingredients = {}
    for count, dish in order_list:
        if dish in dish_ingredients:
            for ingredient in dish_ingredients[dish]:
                ing_name = ingredient['Ingredient']
                if ing_name not in required_ingredients:
                    required_ingredients[ing_name] = {'Unit': ingredient['Unit'], 'Quantity': 0}
                required_ingredients[ing_name]['Quantity'] += ingredient['Quantity'] * count

    ingredients_list = [{'Ingredient': k, 'Unit': v['Unit'], 'Quantity': v['Quantity']} for k, v in required_ingredients.items()]
    
    return ingredients_list

def check_and_update_warehouse(ingredients_needed):
    warehouse = {}
    
    with open(filename3, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            warehouse[row['Product']] = {
                'Unit': row['Unit'],
                'Quantity': float(row['Quantity']),
                'Unit price': float(row['Unit price']),
                'Sum': float(row['Sum'])
            }
    
    for ingredient in ingredients_needed:
        product = ingredient['Ingredient']
        required_quantity = ingredient['Quantity']
        
        if product not in warehouse or warehouse[product]['Quantity'] < required_quantity:
            print(f"Out of stock: {product}")
            return False
    
    for ingredient in ingredients_needed:
        product = ingredient['Ingredient']
        required_quantity = ingredient['Quantity']
        warehouse[product]['Quantity'] -= required_quantity
        warehouse[product]['Sum'] -= required_quantity * warehouse[product]['Unit price']
    
    with open(filename3, 'w', newline='') as csvfile:
        fieldnames = ['N', 'Product', 'Unit', 'Quantity', 'Unit price', 'Sum']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, (product, data) in enumerate(warehouse.items(), start=1):
            writer.writerow({
                'N': i,
                'Product': product,
                'Unit': data['Unit'],
                'Quantity': data['Quantity'],
                'Unit price': data['Unit price'],
                'Sum': data['Sum']
            })
    
    return True

def record_income(income):
    if not os.path.exists(filename4):
        with open(filename4, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Order N', 'Total'])

    with open(filename4, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        with open(filename4, 'r', newline='') as readfile:
            reader = csv.reader(readfile)
            next(reader)  
            order_number = sum(1 for row in reader)
        writer.writerow([order_number + 1, income])