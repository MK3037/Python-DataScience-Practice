'''Given a string s consisting of words and spaces, return the length of the last word in the string'''

s="Luffy is still joyboy"
x=0
for i in range(len(s)):
    x=x+1
    if s[i]==" " :
        x=0
print(x)
