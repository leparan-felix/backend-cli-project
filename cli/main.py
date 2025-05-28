import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services import inventory_service
from database.db import initialize_db


def menu():
    print("\n Inventory Management CLI")
    print("1. Add Product")
    print("2. List Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
   

def main():
    initialize_db()
    while True:
        menu()
        choice = input("\nSelect an option: ")

        if choice == "1":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            inventory_service.add_product(name, quantity, price)
            print(" Product added!")

        elif choice == "2":
            products = inventory_service.list_products()
            for p in products:
                print(p)

        elif choice == "3":
            id = int(input("Product ID to update: "))
            quantity = input("New quantity (leave blank to skip): ")
            price = input("New price (leave blank to skip): ")
            inventory_service.update_product(
                id,
                int(quantity) if quantity else None,
                float(price) if price else None
            )
            print(" Product updated!")

        elif choice == "4":
            id = int(input("Product ID to delete: "))
            inventory_service.delete_product(id)
            print(" Product deleted!")

        elif choice == "5":
            print("Exiting. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
