# Declaring lists
raw_stock = []

# User input for raw materials
raw_items = int(input("How many raw materials would you like to enter? "))

for y in range(raw_items):
    print(f"\n--- Raw Material {y+1} ---")
    Material_name = input("Material name: ")
    Material_amount = int(input("Amount of material): "))
    Total_cost = float(input("Total cost (ugx): "))

    entered_materials = {
        "Material_name": Material_name,
        "Material_amount": Material_amount,
        "Total_cost": Total_cost
    }   

    raw_stock.append(entered_materials)

print("\nThese are the raw materials:")
for x in raw_stock:
    print(x)

# Declaring a list of finished products
finished_stock = []

# User input for finished products
finished_items = int(input("\nHow many finished products would you like to enter? "))

for y in range(finished_items):
    print(f"\n--- Finished Product {y+1} ---")
    Product_name = input("Product name: ")
    Product_amount = int(input("Amount of product: "))
    Total_Market_cost = float(input("Market price (ugx): "))

    entered_list = {
        "Product_name": Product_name,
        "Product_amount": Product_amount,
        "Total_Market_cost": Total_Market_cost
    }   

    finished_stock.append(entered_list)

print("\nThese are the finished products:")
for y in finished_stock:
    print(y)


while True:
    print("\n--- Inventory Management Menu ---")
    print("1. Display Inventory")
    print("2. Update Raw Materials")
    print("3. Update Finished Products")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nRaw Materials:")
        for x in raw_stock:
            print(x)

        print("\nFinished Products:")
        for x in finished_stock:
            print(x)

    elif choice == "2":
        specify = input("\nDo you want to add, remove, or change a raw material,type either(add/remove/change): ").strip().lower()

        if specify == "add":
            print("\n--- Add Raw Material ---")
            Material_name = input("Material name: ")
            Material_amount = int(input("Amount of material: "))
            Total_cost = float(input("Total cost(ugx): "))

            raw_stock.append({
                "Material_name": Material_name,
                "Material_amount": Material_amount,
                "Total_cost": Total_cost
            })
            print("Raw material added.")

        elif specify == "remove":
            remove_raw = input("Enter the name of the raw material to remove: ")
            found = False
            for item in raw_stock:
                if item["Material_name"].lower() == remove_raw.lower():
                    raw_stock.remove(item)
                    print(f"{remove_raw} removed from stock.")
                    found = True
                    break
            if not found:
                print(f"{remove_raw} not found in raw materials.")

        elif specify == "change":
            change_value = input("Enter a value to identify the item to change: ")
            found = False
            for item in raw_stock:
                if change_value.lower() in [str(v).lower() for v in item.values()]:
                    field = input("Which field to change (Material_name / Material_amount / Total_cost)? ").strip()
                    if field in item:
                        new_value = input(f"Enter new value for {field}: ")
                        if field == "Material_amount":
                            new_value = int(new_value)
                        elif field == "Total_cost":
                            new_value = float(new_value)
                        item[field] = new_value
                        print("Item updated.")
                        found = True
                        break
                    else:
                        print("Invalid field name.")
            if not found:
                print(f"No matching item found with value '{change_value}'.")

        else:
            print("Invalid option.")

    elif choice == "3":
        specify = input("\nDo you want to add, remove, or change a finished product,type either(add/remove/change): ").strip().lower()

        if specify == "add":
            print("\n--- Add Finished Product ---")
            Product_name = input("Product name: ")
            Product_amount = int(input("Amount of product: "))
            Total_Market_cost = float(input("Market price(ugx): "))

            finished_stock.append({
                "Product_name": Product_name,
                "Product_amount": Product_amount,
                "Total_Market_cost": Total_Market_cost
            })
            print("Product added.")

        elif specify == "remove":
            remove_finished = input("Enter the name of the finished product to remove: ")
            found = False
            for item in finished_stock:
                if item["Product_name"].lower() == remove_finished.lower():
                    finished_stock.remove(item)
                    print(f"{remove_finished} removed from stock.")
                    found = True
                    break
            if not found:
                print(f"{remove_finished} not found in finished products.")

        elif specify == "change":
            change_value = input("Enter a value to identify the item to change: ")
            found = False
            for item in finished_stock:
                if change_value.lower() in [str(v).lower() for v in item.values()]:
                    field = input("Which field to change (Product_name / Product_amount / Total_Market_cost)? ").strip()
                    if field in item:
                        new_value = input(f"Enter new value for {field}: ")
                        if field == "Product_amount":
                            new_value = int(new_value)
                        elif field == "Total_Market_cost":
                            new_value = float(new_value)
                        item[field] = new_value
                        print("Item updated.")
                        found = True
                        break
                    else:
                        print("Invalid field name.")
            if not found:
                print(f"No matching item found with value '{change_value}'.")

        else:
            print("Invalid option.")

    elif choice == "4":
        print("\nThank you! Exiting Inventory Management System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
