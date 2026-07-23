def GCDbruteforce(x,y):
    ans=1
    for i in range(2,x+1):
        while x%i==0 and y%i==0:
            x=x/i
            y=y/i
            ans*=i

def GCDoptimized(x,y):              #since gcd(x,y)=gcd(x-ay,y)=gcd(r,y) where r=remainder and 
    while y:
        x, y = y, x % y
    return x
def find_list_gcd(numbers):         #this part is for a list of numbers
    if not numbers:
        return 0
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = GCDoptimized(result, numbers[i])
        
        if result == 1:
            return 1
            
    return result

x=3
y=12
print(GCDbruteforce(x,y))
print(GCDoptimized(x,y))

my_numbers = [48, 72, 120, 24]      #for a list of numbers
print(f"The GCD of {my_numbers} is: {find_list_gcd(my_numbers)}")


LCM=x*y/GCDoptimized(x,y)           #since lcm*hcf(x,y)=x*y


"""
================================================================================
                        GCD (GREATEST COMMON DIVISOR) — KEY PROPERTIES
================================================================================

1. GCD as a Building Block
   ----------------------------------------------------------------------------
   The GCD of a set of numbers is the smallest "building block."
   You can construct any number of the form Ax + By using multiples
   of their GCD.

2. Common Divisors Divide GCD
   ----------------------------------------------------------------------------
   Every common divisor of two numbers A and B must also be a
   divisor of their GCD.

3. Linear Combination (Bezout's Identity)
   ----------------------------------------------------------------------------
   The GCD of A and B can be expressed as a linear combination:
       Ax + By = gcd(A, B)
   This is the foundation for the Extended Euclidean Algorithm.

4. GCD with Zero
   ----------------------------------------------------------------------------
       gcd(A, 0) = A

5. Scaling Property
   ----------------------------------------------------------------------------
       gcd(mA, mB) = m * gcd(A, B)
   Corollary: dividing A and B by their GCD makes the results coprime
   (their GCD becomes 1).

6. Adding Multiples
   ----------------------------------------------------------------------------
   Adding or subtracting multiples of B from A does not change the GCD:
       gcd(A, B) = gcd(A ± kB, B)
   This is the logic behind the Euclidean Algorithm.

7. Euclidean Identity
   ----------------------------------------------------------------------------
   The heart of efficient GCD computation:
       gcd(A, B) = gcd(B, A mod B)

8. Multiplicative Property
   ----------------------------------------------------------------------------
   If A1 and A2 are coprime, then:
       gcd(A1 * A2, B) = gcd(A1, B) * gcd(A2, B)

9. Commutative & Associative Properties
   ----------------------------------------------------------------------------
   Commutative:  gcd(A, B) = gcd(B, A)
   Associative:  gcd(A, gcd(B, C)) = gcd(gcd(A, B), C)
   Vital for finding the GCD of entire arrays.

10. Distributive Identity
    ---------------------------------------------------------------------------
        gcd(A, lcm(B, C)) = lcm(gcd(A, B), gcd(A, C))

11. Geometric Interpretation
    ---------------------------------------------------------------------------
    The number of integer points on a line segment from (0, 0) to (A, B)
    on a grid is gcd(A, B) + 1.

12. GCD of Arithmetic Progressions
    ---------------------------------------------------------------------------
    The GCD of a sequence A, A+D, A+2D, ... is simply gcd(A, D).

13. GCD of Factorials
    ---------------------------------------------------------------------------
        gcd(N!, M!) = min(N, M)!

14. GCD of Powers
    ---------------------------------------------------------------------------
        gcd(A^X, A^Y) = A^min(X, Y)

================================================================================
"""
