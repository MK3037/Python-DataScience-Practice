import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac4")
print(os.getcwd())
with open("main",'w') as f:
    f.write('''report_2023.pdf	
vacation_photo.jpg	
budget_notes.txt	
presentation_final_v2.pdf
script_backup.txt	
holiday_video.jpg	
data_archive.zip''')
    
with open("main",'r') as f:
    for line in f:
        filename=line.strip()
        print(filename)
        with open(filename,'w') as g:
            pass
            
os.remove("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\prac4\\main")