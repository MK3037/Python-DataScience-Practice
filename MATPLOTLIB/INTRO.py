from matplotlib import pyplot as plt

print(plt.style.available)                                  #this styles have there own color and grid also along with theme
plt.style.use('ggplot')                                     #try plt.xkcd() , best

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x,dev_y, '.k--', label='All devs')             #fmt=[marker][line][color]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y, label='Python')

plt.title('Median salary by ages')
plt.xlabel('ages')
plt.ylabel('salary(USD)')

plt.legend()
# plt.grid(True)                                             #since we used style
plt.savefig('intro.png')                                   
plt.show()