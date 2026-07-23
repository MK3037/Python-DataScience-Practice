# --- for...else example ---
for i in range(3):
    print(i)
else:
    print("For loop finished successfully!") # Executes [00:01:23]

# --- while...else example ---
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("While loop finished successfully!") # Executes [00:04:39]

# --- BREAK example (Crucial for Interviews) ---
for i in range(5):
    if i == 3:
        break  # Loop is broken here
    print(i)
else:
    print("This will NOT print because of the break.") # [00:03:13]