# 1. Creating a Dictionary (Key-Value Pairs)
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# 2. Accessing Values
# Using brackets (throws KeyError if key doesn't exist)
print(f"Name: {student['name']}")

# Using .get() (Returns 'None' or a custom default instead of an error)
print(f"Phone: {student.get('phone', 'Not Found')}")
print(f"{student}\n")       #phone isnt added with value not found

# 3. Adding and Updating Values
student['phone'] = '555-5555'  # Adds a new key
student.update({'name': 'Jane', 'age': 26})  # Updates multiple values at once

# 4. Removing Values
# Using 'del' to remove a specific key
del student['age']

# Using '.pop()' (removes the key AND returns its value for use)
popped_name = student.pop('name')
print(f"Removed name: {popped_name}")

# Check the number of keys
print(f"Number of keys: {len(student)}")

# Loop through keys and values simultaneously
for key, value in student.items():
    print(f"{key}: {value}")



# keys = ['ones', 'tens', 'hundreds']
# values = [1, 10, 100]

# # zip() pairs them up, dict() turns those pairs into a dictionary
# my_dict = dict(zip(keys, values))




# arr1 = [1, 10, 100]

# # Using a dictionary comprehension
# my_dict = {index: num for index, num in enumerate(arr1)}

# print(my_dict)
# # Output: {0: 1, 1: 10, 2: 100}




# Quick access to components:
# print(student.keys())   -> dict_keys(['courses', 'phone'])
# print(student.values()) -> dict_values([['Math', 'CompSci'], '555-5555'])