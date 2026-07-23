import os
print(os.getcwd())                                  #get current working directory
os.chdir('D:\\Mihir Document\\Mihir studies\\DS') #change current working directory
print(os.getcwd())
print(os.listdir())                                 #list all directory

with open('MIHIR', 'w') as f:                       #file
    f.write("Hello! This file was just created.")
os.remove('D:\\Mihir Document\\Mihir studies\\DS\\MIHIR')

os.rmdir('BILLION')                                 #folder
os.mkdir('BILLION')

os.removedirs('TRILLION\\DOLLAR')                   #multilevelfolder
os.makedirs('TRILLION\\DOLLAR')

# os.rename('old_file_name','new_file_name')
x=input("file name u want to find stat about: ")    #ch8.docx
print(f"\n{os.stat(x)}")                            #to find status of a file 