import csv
import pandas as pd
from tabulate import tabulate

fields = ['N', 'Product', 'Unit','Quantity', 'Unit price','Sum']
filename = "warehouse.csv"
items = [] 

    #print((items[0])['Quantity'])

def main():
    #ვალიდაციაა დასამატებელი თუ სამზარეულოს აინტერესებს და თუ ბუღალტერიას აინტერესებს
    accountant_warehouse()
    #kitchen_warehouse()
    admin_order = input("Add product: ")
    if admin_order == "1":
        new_product()

def accountant_warehouse():
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))
        
def kitchen_warehouse():
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filtered_row = {key: row[key] for key in ['N', 'Product', 'Unit', 'Quantity']}
            items.append(filtered_row)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))

def new_product():
    product_name = input("Name of product:  ").strip()
    unit = input("Name of unit:  ").strip()
    while True:
        try:
            quantity = float(input("Quantity of product: ").strip())
            unit_price = float(input("Price of unit: ").strip())
            sum = quantity * unit_price
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
    
    mydict = [{'N': new_num, 'Product': product_name.title() , 'Unit': unit.title() ,'Quantity': quantity, 'Unit price' : unit_price,'Sum': sum}]
    
    with open(filename, 'a', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if last_num == 0:
            writer.writeheader()
        writer.writerows(mydict)

def drop_product():
    ...



def dish_cost():
    ...


main()
