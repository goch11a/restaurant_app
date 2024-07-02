import csv
from tabulate import tabulate
from collections import Counter
from waiters_mng import get_order, get_ingredients, check_and_update_warehouse, record_income
from menu import new_dish, edit_dish, delete_dish, calculate_dish_costs
from warehouse import kitchen_warehouse,accountant_warehouse, new_product, drop_product
import user

filename = "menu.csv"
filename2 = "dish_ingredients.csv"
filename3 = "warehouse.csv"
filename4 = "incomes.csv"

def main():
    while True:
            try:
                user_checker = int(input("1 - Log in\n2 - Edit user\nChoose number: "))
                break
            except ValueError:
                print("Only digits!")
    if user_checker == 1:
        username = input("Username: ").title()
        password = input("Password: ")
        user_pass, user_role = check_password(username)
        if password == user_pass:
            if user_role == "waiter":
                orders, income = get_order()
                if orders and income:
                    ingredient = get_ingredients(orders)
                    if check_and_update_warehouse(ingredient):
                        record_income(income)
                        print(f"Your order is done. The total price is {income}.")
                    else:
                        print("Unfortunately, we are out of stock.")
            elif user_role == "admin":
                print("1 - Add dish\n2 - Edit dish\n3 - Delete dish\n4 - Dish cost\n5 - Warehouse for kitchan\n6 - Warehouse for manager\n7 - New product\n8 - Drop product")
                while True:
                    try:
                        user_input = int(input("Choose number: "))
                        break
                    except ValueError:
                        print("Only digits!")
                if user_input == 1:
                    new_dish()
                elif user_input == 2:
                    edit_dish()
                elif user_input == 3:
                    delete_dish()
                elif user_input == 4:
                    calculate_dish_costs()
                elif user_input == 5:
                    kitchen_warehouse()
                elif user_input == 6:
                    accountant_warehouse()
                elif user_input == 7:
                    new_product()
                elif user_input == 8:
                    drop_product()
    elif user_checker == 2:
        user.main()    

def check_password(username):
    with open("writer.csv", "r") as f:
        csv_read = csv.DictReader(f)
        for row in csv_read:
            if row["User"] == username:
                return row["Password"],row["Role"]
                 
        return None, None


if __name__ == "__main__":
    main()