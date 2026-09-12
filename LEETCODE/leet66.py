'''You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.'''
a = [9, 8, 9]
def plusOne(digits):
        c=1
        digits=digits[::-1]
        for i in range(len(digits)):
            if c==1:
                digits[i]+=c
                c-=1
                if digits[i]==10:
                    digits[i]=0
                    c=1
                    if i==len(digits)-1:
                        digits.append(1)
            else:
                break
        return digits[::-1]

print(plusOne(a))   