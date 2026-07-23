import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac2")
for f in os.listdir():
    print(f)
    file_name, file_ext=os.path.splitext(f)         #Jupiter - Our Solar System - #6.mp4            

    #Everywhere Python sees a -, it makes a cut and separates the text into pieces.
    f_title, f_course, f_num = file_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = f'{f_num}-{f_title}{file_ext}'
    os.rename(f, new_name)