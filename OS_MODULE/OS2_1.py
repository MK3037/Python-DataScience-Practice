import os
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac2')

with open("mihir", 'w') as f:
    f.write('''Earth - Our Solar System - #1
Jupiter - Our Solar System - #6
Mars - Our Solar System - #4
Mercury - Our Solar System - #2
Neptune - Our Solar System - #8
Saturn - Our Solar System - #7
Uranus - Our Solar System - #9
Venus - Our Solar System - #3
Pluto - Our Solar System - #10''')

with open("mihir", 'r') as f:
    # This loop goes through every line in your reference file
    for line in f:
        # .strip() is crucial because it removes the invisible newline (\n) 
        # character at the end of each line, which isn't allowed in filenames.
        filename = line.strip()
        
        # Make sure the line isn't empty
        if filename:
            # Add an extension (like .mp4) 
            filename = filename + ".mp4"
            
            with open(filename, 'w') as new_file:
                new_file.write("This makes the new file.")
            
            print(f"Created: {filename}")
os.remove('C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac2\\mihir')
