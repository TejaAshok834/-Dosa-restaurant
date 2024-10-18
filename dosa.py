import json
import sys

# Step 1: Read the JSON orders from a file 
def json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        sys.exit(1)

# Function to format phone numbers
def format_phone_number(phone):
    return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

# Step 2: Create a json file customers.json
def create_customer(data):
    customers = {}
    for item in data:
        phone_number = item.get('phone')
        customer_name = item.get('name')
        if phone_number and customer_name:
            formatted_phone_number = format_phone_number(phone_number)
            customers[formatted_phone_number] = customer_name
    # Convert the dict to a json file
    with open('customers.json', 'w') as customers_file:
        json.dump(customers, customers_file, indent=4)
    print("We created customer json file successfully")

# Step 3: Create a json file items.json
def create_items(data):
    items_dict = {}
    for order in data:
        for item in order.get('items', []):
            item_name = item.get('name')
            item_price = item.get('price')
            if item_name and item_price:
                if item_name not in items_dict:
                    items_dict[item_name] = {"price": item_price, "orders": 1}
                else:
                    items_dict[item_name]['orders'] += 1
    with open('items.json', 'w') as items_file:
        json.dump(items_dict, items_file, indent=4)
    print("We created items json file successfully")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <orders_file.json>")
        sys.exit(1)
    
    # Step 1: Read the json file
    orders_file = sys.argv[1]
    orders_data = json_file(orders_file)

    # Step 2: Create customers.json
    create_customer(orders_data)

    # Step 3: Create items.json
    create_items(orders_data)
