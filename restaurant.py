import hashlib
import os
import csv
import bcrypt
import re
from tabulate import tabulate
import pandas as pd

def main():
    if not os.path.isfile("writer.csv"):
        header_()




def header_():
    with open("writer.csv", "w") as file:
        header = ["username", "password", "role"]
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)  

def check_user(suername):
    ...

