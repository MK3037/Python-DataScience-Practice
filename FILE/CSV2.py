import csv
import os
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac3')
print(os.getcwd())

with open('name.csv','r') as csvfile:       #reading simply as a file
    for line in csvfile:
        print(line)


with open('name.csv','r') as csvfile:       #csv speciall
    csv_readerspecial=csv.reader(csvfile)
    for line in csv_readerspecial:
        print(line)
    for line in csv_readerspecial:          #rading column 1 only
        print(line[2])   
    

with open('name.csv','a') as csvfile:       #simply writing as in a normal file
    csvfile.write("\nJohn,Doe,john-doe@bogusemail.com")

with open('name.csv','r') as csvreader:
    csv_readerspecial=csv.reader(csvreader)

    with open('name_newfile.csv','w',newline='') as csvwriter:
        csv_writerspecial=csv.writer(csvwriter,delimiter=',',quoting=csv.QUOTE_ALL)

        for line in csv_readerspecial:
            csv_writerspecial.writerow(line)



# To include csv.QUOTE_ALL, you need to pass it into the quoting parameter of your csv.writer. 
# This will place double quotes around every single value, which is a 
# great way to ensure that special characters (like your # delimiter or any commas) don't break the file structure.

# If you were to open name_newfile.csv in a text editor (like Notepad), it will now look like this:
# "first_name"#"last_name"#"email"
# "John"#"Doe"#"john-doe@bogusemail.com"
# "Corey"#"Schafer"#"coreymschafer@gmail.com"
    
    # # Open the new file with newline='' to fix the blank rows
    # with open('name_newfile.csv', 'w', newline='') as csvwriter:
        
    #     # Add quoting=csv.QUOTE_ALL here
    #     csv_writerspecial = csv.writer(
    #         csvwriter, 
    #         delimiter='#', 
    #         quoting=csv.QUOTE_ALL
    #     )

# Why do this?
# Safety: If someone’s email was john#doe@email.com, the # inside the email would confuse the computer. 
# By wrapping it in quotes—"john#doe@email.com"—the computer knows that the # inside the quotes is just text, 
# not a column separator.

# Consistency: Every field is treated exactly the same, which makes it easier for other programs (like SQL databases) 
# to import the data correctly.