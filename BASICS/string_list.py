x=["Hi","How"]
x=x[::-1]
x=' '.join(x)       #converting list back to srting
print(x)

#flipping case of letters in string and then reversing it
x = x.swapcase()
x=list(x)
print(x)
x=x[::-1]
print(x)