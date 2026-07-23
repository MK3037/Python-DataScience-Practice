def smart_counter():
    count = 1
    print("--- Starting the counter ---")
    while count <= 3:
        yield f"Result: {count}"
        count += 1
        print("--- Waking up for the next count ---")

counter = smart_counter()

print(next(counter)) # Runs until first yield
print(next(counter)) # Resumes from first yield, runs to second