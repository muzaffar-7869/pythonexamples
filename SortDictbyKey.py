# Sort a list of dictionaries by a specific key
# Sample list of dictionaries
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]

# Sort the list of dictionaries by the 'age' key
sorted_data = sorted(data, key=lambda x: x['age'])

# Print the sorted list of dictionaries
for item in sorted_data:
    print(item)
