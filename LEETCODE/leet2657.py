class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        # Kept your exact variable names, but changed lists to sets!
        C = set()
        D = set()
        ans = []
        
        # We keep your exact main loop
        for i in range(len(A)):
            C.add(A[i])  # Using .add() instead of .append() for sets
            D.add(B[i])
            
            count = 0
            
            # --- THE SECOND LOOP IS GONE! ---
            # Instead of looping through C manually, we just look at what 
            # elements C and D have in common instantly using an intersection (&).
            #The & operator (intersection) belongs strictly to sets in Python. Lists don't know how to use it.
            common_elements = C & D
            count = len(common_elements)
            
            ans.append(count)
            
        return ans
 
sol = Solution()

test_A = [1, 3, 2, 4]
test_B = [3, 1, 2, 4]

print("Input A:", test_A)
print("Input B:", test_B)

final_ans = sol.findThePrefixCommonArray(test_A, test_B)

print("Result: ", final_ans)
# Output: [0, 2, 3, 4]