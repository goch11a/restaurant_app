import csv
import pandas as pd
from tabulate import tabulate

fields = ['N', 'Product', 'Unit','Quantity', 'Unit price','Sum']
filename3 = "warehouse.csv"
items = [] 

   


def accountant_warehouse():
    with open(filename3, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))
        
def kitchen_warehouse():
    with open(filename3, newline='') as csvfile:
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
        with open(filename3, 'r', newline='') as csvfile:
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
    
    with open(filename3, 'a', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        if last_num == 0:
            writer.writeheader()
        writer.writerows(mydict)

def drop_product():
    with open(filename3, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))

    while True:
        try:
            order_number = int(input("Enter the order number of the product to drop: ").strip())
            break
        except ValueError:
            print("Please enter a valid order number.")

    try:
        df = pd.read_csv(filename3)
        if order_number in df['N'].values:
            df.loc[df['N'] == order_number, ['Quantity', 'Sum']] = 0
            df.to_csv(filename3, index=False)
            print("Product quantity updated successfully.")
        else:
            print("Order number not found.")
    except FileNotFoundError:
        print("Warehouse file not found.")



