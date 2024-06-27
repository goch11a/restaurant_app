import os
import csv

def main():
    if not os.path.isfile("writer.csv"):
        header_()




def header_():
    with open("writer.csv", "w") as file:
        header = ["username", "password", "role"]
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)  

def check_user(suername):
    print("irakli")

