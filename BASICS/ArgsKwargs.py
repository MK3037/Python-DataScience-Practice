def super_function(*args, **kwargs):               #int func(int... x) in java for random number of inputs in a function
    print(f"Positional arguments (args): {args}")
    print(f"Keyword arguments (kwargs): {kwargs}")
    print(len(kwargs))  
    print("\n")
    
super_function(1, 2, 3, name="Alice", age=25, job="Dev")

#When you run super_function(1, 2, 3, name="Alice"), Python essentially does this internally:
# Scans arguments: "I see three plain values and one named value."
# Creates Tuple: args = (1, 2, 3)
# Creates Dictionary: kwargs = {"name": "Alice"}
# Hands them to your code.

def higher_level(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['Maths','Arts']
info={'name':'John', 'age':22}

higher_level(courses,info)
higher_level(*courses,**info)
