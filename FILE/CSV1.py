import csv
import os

folder_path = r'C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac3'
file_name = 'name.csv'
full_path = os.path.join(folder_path, file_name)

# 2. Check if the file exists before trying to open it
if os.path.exists(full_path):
    print(f"File found at: {full_path}")
    
    # 3. Read using DictReader 
    with open(full_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Define output path
        output_file = os.path.join(folder_path, 'name_modified.csv')
        
        # 4. Write to a new file in the same directory
        fieldnames = ['first_name', 'last_name', 'email']
        
        with open(output_file, 'w', newline='') as new_file:
            # Using Tab delimiter as shown in the video 
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            
            csv_writer.writeheader()
            
            for line in csv_reader:
                print(f"Processing: {line['first_name']}")
                csv_writer.writerow(line)
                
    print(f"\nSuccess! Modified file saved to: {output_file}")

else:
    print(f"Error: The file {file_name} was not found in {folder_path}")
    # List files in the directory to help you debug
    print("Files actually in this folder:", os.listdir(folder_path))