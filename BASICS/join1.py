# The separator is a string (like a comma, space, or hyphen)
words = ["Python", "is", "awesome"]

# Basic join with a space
sentence = " ".join(words)
print(f"Basic join: {sentence}") 
# Output: Python is awesome


# Joining numbers (Note: All elements MUST be strings)
numbers = [1, 2, 3, 4]
# This would cause a TypeError:
# print("-".join(numbers)) 

# The correct approach using a generator expression:
formatted_nums = "-".join(str(n) for n in numbers)
print(f"Formatted numbers: {formatted_nums}")
# Output: 1-2-3-4

# Using join for multi-line output (common for reports)
lines = ["Line 1", "Line 2", "Line 3"]
report = "\n".join(lines)
print(f"Multi-line string:\n{report}")




# Poor practice (don't do this for large datasets):
# result = ""
# for char in large_list: result += char

# Best practice (Join is memory efficient):
def build_large_string(data):
    return "".join(data)

data_chunks = ["part1", "part2", "part3"]
print(f"Efficient join: {build_large_string(data_chunks)}")




matrix = [["a", "b"], ["c", "d"], ["e", "f"]]

# Flattening and joining
flat_string = ", ".join("".join(sub) for sub in matrix)
print(f"Nested join: {flat_string}")
# Output: ab, cd, ef