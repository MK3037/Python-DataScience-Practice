class Solution(object):
    def reverseBits(self, n):
        x = bin(n)[2:]              #converting int n to bits x using bin. but bin give output like '0b1101', so we have to strip of first two 0b

        # LeetCode treats numbers as rigid 32-bit blocks. We must pad with zeros 
        # BEFORE reversing so that the hidden leading zeros properly flip 
        # to the back and change the final number's value.
        x = x.zfill(32)
        x = x[::-1]                 #reversing bits as it was asked

        return int(x, 2)            #converting bits with base 2 back to int

# --- Output Entry ---
tester = Solution()
print(tester.reverseBits(4))  # Output: 536870912