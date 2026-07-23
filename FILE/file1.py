import time
# --- CONCEPT 1: READING FILES ---
# Using the 'with' context manager is best practice as it closes the file automatically.
with open('file2.txt', 'r') as f:
    
    # Method A: Read all at once (Not recommended for very large files as file pointer has to be changed constatnly)
    # f_contents = f.read() 
    
    # Method B: Read as a list of lines
    # f_contents = f.readlines()
    # print(f_contents)

    # Method C: Efficiently iterate line-by-line (Best for memory)
    print("--- Reading Line by Line ---")
    for line in f:
        print(line, end='') # 'end' removes the extra newline from the print function

# --- CONCEPT 2: NAVIGATION (SEEK & TELL) ---
with open('file2.txt', 'r') as f:
    size_to_read = 10
    
    # Read a specific number of characters
    f_contents = f.read(size_to_read)
    print(f"\n\nFirst 10 characters: {f_contents}")
    
    # .tell() shows your current cursor position in the file
    print(f"Current Position: {f.tell()}")
    
    # .seek() moves the cursor back to a specific position (0 is the start)
    f.seek(0)
    print(f"Back at position {f.tell()} after seek(0)")

# --- CONCEPT 3: WRITING FILES ---
# 'w' creates a new file or overwrites an existing one.
with open('file2_copy.txt', 'w') as f:
    f.write('Python Programming')
    # Using seek while writing allows you to overwrite specific parts
    f.seek(0)
    f.write('J')        # 'Python' becomes 'Jython'
    time.sleep(5)      # open this file within 10 sec and see
    
# --- CONCEPT 4: COPYING TEXT & BINARY FILES ---
# Copying a text file
with open('file2.txt', 'r') as rf:
    with open('file2_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

print("\nOperations completed successfully.")