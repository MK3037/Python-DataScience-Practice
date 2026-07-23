'''STRING: immutable, ordered'''
print("hi how are 'you'")   #You can use quotes inside a string,the string:
#as long as they don't match the quotes surrounding

a = """Lorem ipsum dolor sit amet,              
consectetr adipiscing elit"""
b = " mihir is a billionaire"
print(f"simply printing a {a}")                #simply printing a
print(a[0:10])          #printing 0 to 9th character of string a
print(a.upper())        #convertinf string a to all upper case
print(a.find('Lorem'))
c=a.replace("Lorem","Mihir")       
print(c)

print(a[-3:-1])         #similarly print(a.lower()) for all lower case

print(a+b)

a="1"
b="3"
c="-3"
c=abs(int(c))           #converting -3 to +3 using abs
print(int(a)+int(b)+c)

d=f"the king {a}"

print(f"my name is {a}")        #f string