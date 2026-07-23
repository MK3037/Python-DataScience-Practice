from matplotlib import pyplot as plt       
import numpy as np                         
plt.style.use('ggplot')                                                           

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_idexes=np.arange(len(ages_x))                             #cause showing three bars would overall one over other 
width=0.25                                                  #so we have to do this width and idexes thing

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_idexes-width, dev_y, width=width,label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_idexes, py_dev_y,width=width, label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_idexes+width, js_dev_y, width=width,label="JavaScript")


plt.title('Median salary by ages')
plt.xlabel('ages')
plt.ylabel('salary(USD)')

plt.legend()
plt.savefig('intro.png')                                   
plt.show()