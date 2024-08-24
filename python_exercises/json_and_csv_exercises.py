# import json
#
#
# def parse_json(json_string):
#     try:
#         # Parse the JSON string and return the resulting dictionary
#         data = json.loads(json_string)
#         return data
#     except json.JSONDecodeError:
#         # Handle the case where the JSON is not valid
#         print("Invalid JSON string.")
#         return None
#
#
# # Example usage:
# json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
# parsed_data = parse_json(json_string)
# print(parsed_data)

# -------------------------------------------------------------------

# import json
#
#
# def get_value_from_json(json_string, key):
#     try:
#         # Parse the JSON string into a dictionary
#         data = json.loads(json_string)
#
#         # Return the value associated with the given key (if it exists)
#         return data.get(key, None)  # Returns None if the key is not found
#     except json.JSONDecodeError:
#         # Handle the case where the JSON is not valid
#         print("Invalid JSON string.")
#         return None
#
#     # Example usage:
#
#
# json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
# key = 'age'
# value = get_value_from_json(json_string, key)
# print(value)  # Output: 30

# ---------------------------------------------------------------------

# import json
#
# def update_json(json_string, key, value):
#     try:
#         # Parse the JSON string into a dictionary
#         data = json.loads(json_string)
#
#         # Update or add the key-value pair
#         data[key] = value
#
#         # Convert the dictionary back to a JSON string
#         updated_json_string = json.dumps(data)
#         return updated_json_string
#     except json.JSONDecodeError:
#         # Handle the case where the JSON is not valid
#         print("Invalid JSON string.")
#         return None
#
# # Example usage:
# json_string = '{"name": "Alice", "age": 30}'
# key = 'city'
# value = 'New York'
# updated_json = update_json(json_string, key, value)
# print(updated_json)  # Output: {"name": "Alice", "age": 30, "city": "New York"}

# ------------------------------------------------------------------------------

# import json
# from collections import defaultdict
#
# def count_unique_values(json_string):
#     try:
#         # Parse the JSON string into a list of dictionaries
#         data = json.loads(json_string)
#
#         # Create a defaultdict to count occurrences of each value
#         value_counts = defaultdict(int)
#
#         # Iterate through the list and count each unique value
#         for item in data:
#             if 'color' in item:
#                 value_counts[item['color']] += 1
#
#         # Convert defaultdict to a regular dict before returning
#         return dict(value_counts)
#
#     except json.JSONDecodeError:
#         # Handle the case where the JSON is not valid
#         print("Invalid JSON string.")
#         return None
#
# # Example usage:
# json_string = '[{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]'
# result = count_unique_values(json_string)
# print(result)  # Output: {'red': 2, 'blue': 1, 'green': 1}

# ------------------------------------------------------------------------

# import json
#
#
# def merge_json(json_string1, json_string2):
#     try:
#         # Parse the first JSON string into a dictionary
#         data1 = json.loads(json_string1)
#         # Parse the second JSON string into a dictionary
#         data2 = json.loads(json_string2)
#
#         # Merge both dictionaries
#         merged_data = {**data1, **data2}
#
#         # Convert the merged dictionary back to a JSON string
#         merged_json_string = json.dumps(merged_data)
#         return merged_json_string
#
#     except json.JSONDecodeError:
#         # Handle the case where the JSON is not valid
#         print("Invalid JSON string.")
#         return None
#
#     # Example usage:
#
#
# json_string1 = '{"name": "Alice", "age": 30}'
# json_string2 = '{"city": "New York", "country": "USA"}'
# result = merge_json(json_string1, json_string2)
# print(result)  # Output: {"name": "Alice", "age": 30, "city": "New York", "country": "USA"}

# -------------------------------------------------------------------------------

# import json
# import csv
# from io import StringIO
#
#
# def json_to_csv(json_string):
#     try:
#         # Parse the JSON string into a list of dictionaries
#         data = json.loads(json_string)
#
#         # Create a StringIO object to write CSV to a string
#         output = StringIO()
#         writer = csv.DictWriter(output, fieldnames=data[0].keys())
#
#         # Write the header
#         writer.writeheader()
#
#         # Write the data
#         writer.writerows(data)
#
#         # Get the CSV string from StringIO
#         csv_string = output.getvalue()
#         output.close()
#
#         return csv_string
#
#     except json.JSONDecodeError:
#         print("Invalid JSON string.")
#         return None
#
#     # Example usage:
#
#
# json_string = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]'
# result = json_to_csv(json_string)
# print(result)

# -----------------------------------------------------------------------

# import csv
#
#
# def write_dicts_to_csv(data, filename):
#     if not data:
#         print("The input list is empty.")
#         return
#
#         # Get the header from the keys of the first dictionary
#     header = data[0].keys()
#
#     # Open the file in write mode
#     with open(filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=header)
#
#         # Write the header
#         writer.writeheader()
#
#         # Write the rows
#         writer.writerows(data)
#
#     print(f"Data written to {filename}")
#
#
# # Example usage:
# data = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "San Francisco"},
#     {"name": "Charlie", "age": 35, "city": "Los Angeles"}
# ]
#
# write_dicts_to_csv(data, 'output.csv')

# -------------------------------------------------------------------------

# import csv
#
#
# def sum_column_in_csv(file_path, column_name):
#     total_sum = 0
#     row_count = 0
#
#     try:
#         with open(file_path, mode='r', newline='', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#
#             # Check if the column exists in the header
#             if column_name not in reader.fieldnames:
#                 print(f"Column '{column_name}' not found in the CSV file.")
#                 return None
#
#             for row in reader:
#                 try:
#                     value = float(row[column_name])  # Convert the value to float
#                     total_sum += value
#                     row_count += 1
#                 except ValueError:
#                     print(f"Value '{row[column_name]}' in row {row_count + 1} is not a number and will be skipped.")
#                     continue  # Skip non-numeric values
#
#         print(f"Sum of column '{column_name}': {total_sum}")
#         return total_sum
#
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#         return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
#
#     # Example usage:
# # Make sure the file 'data.csv' exists with appropriate data.
# # sum_column_in_csv('data.csv', 'age')  # Replace 'age' with the target column name.

# ------------------------------------------------------------------------------

