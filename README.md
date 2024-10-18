Restaurant Order Processing Tool
Overview:
This Python script helps a restaurant process its order data, which is provided in a JSON format. The script reads customer information and their orders, and then generates two output files:

customers.json: This file contains customer phone numbers paired with their names.
items.json: This file includes details about each item ordered, such as its price and how many times it has been ordered.

How It Works:
The script processes a JSON file containing individual orders. Each order includes:
Customer Information: A phone number and name.
Order Details: A list of items the customer purchased, each with a name and price.

The script will generate two JSON files:
customers.json: Contains a dictionary where the phone numbers are the keys, and the customer names are the values.
items.json: Contains a dictionary where item names are the keys. Each item has a sub-dictionary showing the price and how many times it was ordered.

Design and Implementation:
Customers Data: The script extracts customer phone numbers and names from each order and stores them in a dictionary. The phone numbers are formatted as xxx-xxx-xxxx before being written to the customers.json file.
Items Data: The script analyzes each item ordered. It creates a dictionary where the item names are the keys. For each item, it records the price and how many times the item was ordered. The result is written to the items.json file.

Usage Instructions:
we need to place our JSON file containing the orders in the same directory as the script or provide its full path.
Run the script using the command:python <script_name.py>  <order_file.json> for me it is python dosa.py example_orders.json

Error Handling:
If the input file is not found, the script will display an error message and stop execution.