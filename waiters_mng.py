import csv
from tabulate import tabulate
from collections import Counter

filename = "menu.csv"
filename2 = "dish_ingredients.csv"
filename3 = "warehouse.csv"
items = []

def main():
    ...#მისასალმებელი ტექსტი და მერე მენიუ
    print("Hello, welcome to Burger Bar Krikina")
    get_order()
    

def get_order():

    #ხსნის მენიუს
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))
    
    #იღებს შეკვეთას
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
            order_sum.append(float(order_price))
            continue
        else:
            order = (items[order_num - 1])['Dish']
            order_list.append(order)
            order_price = (items[order_num - 1])['Price']
            order_sum.append(float(order_price))
            break
    
        
    sum_pay = sum(order_sum)
    dish_counts = Counter(order_list)

    table_data = []
    for dish, count in dish_counts.items():
        table_data.append([count, dish])

    
    table = tabulate(table_data, headers=["Quantity", "Dish"], tablefmt="grid")

    print(table)

    # Print the total sum
    print(f"Total {sum_pay}Lari")
    return table_data, sum_pay 
    #რაოდენობა კერძის უნდა წავიდეს ინგრედიენტებში, დაითვალოს წავიდეს მარაგებში და გამოაკლდეს და დააფდეითდეს
    #ჯამი უნდა წავიდეს შემოსავლების აღრიცხვაში

main()