'''You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.'''
a = [9, 8, 9]
a = a[::-1]      # Reverse: [9, 9, 9]
a[0] = a[0] + 1  # First element becomes 10

for i in range(len(a)):
    if a[i] == 10:
        a[i] = 0
        # Check if there is a next element to carry to
        if i + 1 < len(a):      #till second last 
            a[i+1] = a[i+1] + 1
        else:
            # If we are at the end, append the carry instead
            a.append(1)

a = a[::-1] 
print(a)   