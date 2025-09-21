#!/usr/bin/env python3

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer (e.g. 5).")

# المطلوب: المتغير اسمه number
number = get_int("Enter a number to see its multiplication table: ")

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
