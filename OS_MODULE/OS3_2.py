import shutil
import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac4")
for f in os.listdir():
    if os.path.isfile(f):           #to make sure we arent doing this on folder when run second time
        file_name, file_ext = os.path.splitext(f)
        folder = file_ext[1:]       # remove dot
        if folder not in os.listdir():
            os.mkdir(folder)

current=os.getcwd()
for f in os.listdir():
    if os.path.isfile(f):           #to make sure we arent doing this on folder when run second time
        file_name, file_ext = os.path.splitext(f)
        folder = file_ext[1:]       # remove dot

        # source=f"C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac4\\{f}" 
        source=os.path.join(current,f)
        # destination=f"C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac4\\{folder}"
        destination=os.path.join(current,folder)
        shutil.move(source, destination)        #moving f inside folder