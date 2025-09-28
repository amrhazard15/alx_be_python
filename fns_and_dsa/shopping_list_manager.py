
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
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"✅ '{item}' has been added to your shopping list.")

        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("🛒 Your shopping list is empty.")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
