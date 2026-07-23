import os
print(os.getcwd())
pa='C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac2'
os.chdir(f'{pa}')
print(os.getcwd())
print(os.path.basename(pa))
print(os.path.dirname(pa))

f='Jupiter - Our Solar System - #6.mp4'
filename,fileext=os.path.splitext(f)
print(filename)

# for f in os.listdir():
#     # print(f)
#     filename,fileext=os.path.splitext(f)
#     print(filename)