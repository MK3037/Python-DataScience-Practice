def smallestPalindrome(s):
        x = list(s)
        n = len(s) // 2  
        for i in range(n):                      #sorting first half
            for j in range(n - 1 - i):
                if x[j] > x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]

        first_half = x[:n]

        if len(s) % 2 == 0:
            return "".join(first_half + first_half[::-1])
        else:
            mid = s[len(s) // 2]
            return "".join(first_half + [mid] + first_half[::-1])

s="babab"
print(smallestPalindrome(s))

#The middle character (only exists when n is odd) has no partner — it's not part of any pair, 
# it just sits alone in the dead center. There's nothing to compare it against or swap it with; 
# it doesn't affect the pairs on either side of it, and its own value can't change 
# (whatever letter was in the middle stays in the middle — you're not adding/removing characters, just rearranging pairs). 
# So sorting is meaningless for it — you just read it directly with s[n // 2] and 
# drop it into the center untouched.
#REASON WHY WITHOUT SORTING UPTO MIDDLE ELEMENT WE STILL GOT MID CORRECT 