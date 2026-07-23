'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.'''

s = "A man, a plan, a canal: Panama"
s=s.lower()
print(s)
#a man, a plan, a canal: panama
first=0
last=len(s)-1
palindrom=True

while first<last:
    while first<last and not s[first].isalpha():           # or we can check if s[first] ascii value is between 97 and 122
        first=first+1
    while first<last and not s[last].isalpha():
        last=last-1
    if s[first]!=s[last]:
        print('its not a palindrom')
        palindrom=False
        break
    else:
        first+=1
        last-=1

if palindrom==True:
    print('its a palindrom')