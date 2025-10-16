import csv
import os

FILE_NAME = "expenses.csv"

# Create file if it doesnt  exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Note"])

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (food, travel, etc.): ")
    note = input("Add a note: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, note])
    print("Expense added successfully!\n")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        print("\n--- Expenses ---")
        for row in reader:
            print(f"€{row[0]} | {row[1]} | {row[2]}")
        print()

def show_total():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[0])
    print(f"\n Total spent: €{total}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Bye! ")
        break
    else:
        print("Invalid choice.\n")
