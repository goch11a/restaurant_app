import hashlib
import os
import csv
import bcrypt
import re
from tabulate import tabulate
import pandas as pd

def main():
    username = input("enter your username: ").title()
    if os.path.isfile("writer.csv"):
        chek = check_user(username)
        if chek:
            ad_password = input("eneter password of admin: ")           
            admin_pasword = check_password(username)
                  
            if admin_pasword != ad_password:
                print("invalid identification")
                
            else:
                print("valid identification")
                total()       
        
    else:

        while True:
            admin = input("Enter your role: ")
            if admin != "admin":
                print("You can't register without admin rights.")
                
            else:
                print("You can register, edit, and delete people.")  
                
                while True:
                    password = input("Enter your password: ")
                    lvl = validate_password(password)
                    
                    if lvl == -1:
                        print("Not a valid password")
                        continue
                    else:
                        print("Valid password")
                        
                        
                        add_admin(username, password, admin)
                        total()
                        break
            break
                
                    
                    
                
                    

        
    
                           
                    

def validate_password(password):
    if len(password) <= 8:
        return -1
    elif not re.search("[a-z]", password):
        return -1
    elif not re.search("[A-Z]", password):
        return -1
    elif not re.search("[0-9]", password):
        return -1
    elif not re.search(r"[!#$%&'()*+, -./:;<=>?@[\]^_`{|}~]", password):
        return -1
    return 0

def editor():
    items = []
    
    with open("writer.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))
    
    while True:
        try:
            user = int(input("Choose order of user, which you want to change: ").strip())
            break
        except ValueError:
            print("Only digits!")   
    
    while True:    
        change_item = input("If you want to change User name type U\nIf you want to change Password type P\nif you want to change role type R\n\nType U/P/R: ").upper()
        if change_item in ["U", "P", "R"]:
            break
    
    user_position = user - 1
    if change_item == "U":
        change = "User"
        new_value = (input("Enter new value: ").title()).strip()
    elif change_item == "P":
        change = "Password"
        new_password = input("Enter new value: ").strip()
        bytes = new_password.encode('utf-8')                
        salt = bcrypt.gensalt() 
        new_value = bcrypt.hashpw(bytes, salt)
         
    else:
        change = "Role"
        new_value = input("Enter new value: ").strip()

    df = pd.read_csv("writer.csv")
    df.loc[user_position, change] = new_value
    df.to_csv("writer.csv", index=False)

def delete():
    items = []
    with open("writer.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            items.append(item)
    
    if items:
        print(tabulate(items, headers="keys", tablefmt="grid"))

    while True:
        try:
            user = int(input("Choose order of user, which you want to delete: ").strip())
            break
        except ValueError:
            print("Only digits!")
        
    items.pop(user - 1)

    with open("writer.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["N", "User", "Password", "Role"])
        writer.writeheader()
        for n, i in enumerate(items):
            i['N'] = n + 1
            writer.writerow(i)



def add_admin(username, password, role):
    try:
        with open("writer.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            if rows:
                last_num = int(rows[-1]['N'])
            else:
                last_num = 0
    except FileNotFoundError:
        last_num = 0
    
    new_num = last_num + 1
    mydict = [{'N': new_num, "User": username.title(), "Password": password.strip(), "Role": role}]
    
    with open("writer.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["N", "User", "Password", "Role"])
        if last_num == 0:
            writer.writeheader()
        writer.writerows(mydict)
        print("registration saccsessful")


def add_user(username, password, role):
    try:
        with open("writer.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            if rows:
                last_num = int(rows[-1]['N'])
            else:
                last_num = 0
    except FileNotFoundError:
        last_num = 0
    
    new_num = last_num + 1
    mydict = [{'N': new_num, "User": username.title(), "Password": password.strip(), "Role": role}]
    
    with open("writer.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["N", "User", "Password", "Role"])
        if last_num == 0:
            writer.writeheader()
        writer.writerows(mydict)
        print("registration saccsessful")        

def check_password(username):
    with open("writer.csv", "r") as f:
        csv_read = csv.DictReader(f)
        for row in csv_read:
            if row["User"] == username:
                return row["Password"]
        return None

def check_user(username):
    with open("writer.csv", "r") as f:
        csv_read = csv.DictReader(f)
        for row in csv_read:
            if row["User"] == username:
                return row["User"]

        return None
    


def total():
        register = input("Do you want to register a user? (yes/no): ")
        if register.lower() == "yes":   
            user = input("Enter name: ")
            psw = input("Enter password: ")
            role = input("Enter role: ")
            add_user(user, psw, role)
        while True:
            register_2 = input("Do you want to register more user? (yes/no): ")
            if register_2 == "yes":
                user = input("Enter another name: ")
                psw = input("Enter another password: ")
                role = input("Enter new role: ")
                add_user(user, psw, role)
                continue
            else:
                break

           
        
        deleted = input("Do you want to delete a user or admin? (yes/no): ")
        if deleted.lower() == "yes":
            delete()                               
        
        
        edit = input("Do you want to edit a user or admin? (yes/no): ")  
        if edit.lower() == "yes":
            editor()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    main()









