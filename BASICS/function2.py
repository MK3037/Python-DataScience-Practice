'''BUILT IN FUNCTIONS'''
print(abs(-10.5))                   #Return the absolute value of a number.
result = all([True, True, False])   #Return True if all elements of the iterable are true. long chain of and.
result = any([True, True, False])   #Return True if any element of the iterable is true. If the iterable is empty, return False.
print(ord('a'))                     #Return ascii value
print(chr(97))                      #Return the string representing a character with the specified Unicode code point.Invers of ord.
print(hex(-25))                     #Convert an integer number to a lowercase hexadecimal string prefixed with “0x”
print(bin(-25))                     #Convert an integer number to a binary string prefixed with “0b”.
print(int('FACE',16))               #Return an integer object constructed from a number or a string, or return 0 if no arguments are given.
print(bool(25==25))                 #Return a Boolean value, i.e. one of True or False
print(divmod(5,2))                  #Result is the same as (a // b, a % b) in tupple
print(pow(2,4))                     #Return base to the power exp
print(round(2.6787348,2))           #Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.