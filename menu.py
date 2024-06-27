#'kitchen management'- ის add new dish და edit dish ფუნქციები არის ეს ორი

import csv
import pandas as pd
from tabulate import tabulate

fields = ['N', 'Dish', 'Price']
filename = "menu.csv"


def main():
    num = input("num: ")
    if num == "1":
        new_dish()
    else:
        edit_dish()


def new_dish():
    dish_name = input("Name of dish:  ").strip()
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


def edit_dish():
    items = []
    
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
        except ValueError :
            print("Only digits!")   
    while True:    
        try:
            change_item = input("If you want to change Dish name type D\nIf you want to change Price name type P\n\nType D/P: ").upper()
            if change_item in ["D", "P", "DISH", "PRICE"]:
                break
        except ValueError:
            print("Enter valid input!")
    
    dish_position = dish_order - 1
    if change_item in ["D","Dish"]:
        cheange = "Dish"
        new_dish_value = (input("Enter new value: ").title()).strip()
    else:
        cheange = "Price"
        while True:
            try:
                new_dish_value = int(input("Enter new value: ").strip())
                break
            except ValueError :
                print("Only digits!")
    
    df = pd.read_csv(filename)
    df.loc[dish_position, cheange] = new_dish_value
    df.to_csv(filename, index=False)


main()