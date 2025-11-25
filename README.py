inventory = []

while True:
    print("\nInventory Management System")
    print("+----+------------------------------------+")
    print("|    |           Action                   |")
    print("+----+------------------------------------+")         
    print("| 1  | Add Product (Sack of Rice)         |")
    print("| 2  | Update Product                     |")
    print("| 3  | Delete Product                     |")
    print("| 4  | Search Product                     |")
    print("| 5  | Generate Report                    |")
    print("| 6  | Exit                               |")
    print("+----+------------------------------------+")
     
        
             
    choice = input("Select an option (1-6): ")
    


    if choice == '1':  
        name = input("Enter rice type: ")
        quantity = int(input("Enter quantity in sacks: "))
        reorder_level = int(input("Enter reorder level in sacks: "))
        inventory.append([name, quantity, reorder_level])
        print(f"Added {quantity} sacks of '{name}'.")

    elif choice == '2':
        print("\nCurrent Inventory:")
        print("+------------------+----------------+----------------------+")
        print("| Rice Type        | Quantity       | Reorder Level        |")
        print("+------------------+----------------+----------------------+")
        for item in inventory:
            print(f'| {item[0]:<16} | {item[1]:<14} | {item[2]:<20} |')
        print("+------------------+----------------+----------------------+")
        if not inventory:
            print(f'No products in inventory.')
        
        name = input("Enter rice type to update: ")
        for item in inventory:
            if item[0] == name:
                item[1] = int(input("Enter new quantity in sacks: ")).lower()
                update_reorder = input("Do you want to update the reorder level? (yes/no): ").lower()
                if update_reorder == 'yes':
                    item[2] = int(input("Enter new reorder level in sacks: "))
                print(f"Updated '{name}'.")
                break
        else:
            print(f"Rice type '{name}' not found.")

    elif choice == '3': 
        print("\nCurrent Inventory:")
        print("+------------------+----------------+----------------------+")
        print("| Rice Type        | Quantity       | Reorder Level        |")
        print("+------------------+----------------+----------------------+")
        for item in inventory:
            print(f"| {item[0]:<16} | {item[1]:<14} | {item[2]:<20} |")
        print("+------------------+----------------+----------------------+")

        if not inventory:
            print("No products in inventory.")
        name = input("Enter rice type to delete: ").lower()
        for item in inventory:
            if item[0] == name:
                inventory.remove(item)
                print(f"Deleted '{name}'.")
                break
        else:
            print(f"Rice type '{name}' not found.")

    elif choice == '4':  
        name = input(("Enter rice type to search: ")).lower()
        for item in inventory:
            if item[0] == name:
                print(f"Found: {item[0]} - Quantity: {item[1]} sacks, Reorder Level: {item[2]} sacks")
                break
        else:
            print("Sorry, that rice type is not in the inventory.")

    elif choice == '5':  
        print("\nInventory Report:")
        print("+------------------+----------------+----------------------+")
        print("| Rice Type        | Quantity       | Reorder Level        |")
        print("+------------------+----------------+----------------------+")
        for item in inventory:
            print(f"| {item[0]:<16} | {item[1]:<14} | {item[2]:<20} |")
        print("+------------------+----------------+----------------------+")
        if not inventory:
            print("No products in inventory.")

    elif choice == '6': 
        print("Exiting the Inventory Management System.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
        
               end
        
    
