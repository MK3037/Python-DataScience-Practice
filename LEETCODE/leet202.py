'''A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not'''
def is_happy(n):
    # Set to store numbers we've seen to detect infinite loops
    seen_numbers = set()
    
    # Continue until n becomes 1 or we hit a loop
    while n != 1:
        # If the number has appeared before, it's a cycle
        if n in seen_numbers:
            return False
        
        seen_numbers.add(n)
        
        # Calculate sum of squares of digits
        sum_of_squares = 0
        while n > 0:
            digit = n % 10
            sum_of_squares += digit ** 2
            n //= 10
        
        # Update n with the new sum
        n = sum_of_squares
        
    return True

number = 19
if is_happy(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")