def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == 3:
            print("Your Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == 4:
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
