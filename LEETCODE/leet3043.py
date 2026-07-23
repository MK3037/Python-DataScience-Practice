arr2 = [17, 11]
arr1 = [10]

# --- 1. PREFIX GENERATION FOR ARR1 ---
# ERROR IN ORIGINAL: You only broke down arr2 into prefixes, leaving arr1 as full numbers.
# For [10] and [17], the common prefix is "1". But your code tried to compare 10 == 1 or 10 == 17, which failed.
# SOLUTION: We must break down BOTH arrays into prefixes. We'll use a mathematical Set for speed.
prefixes_arr1 = set()
for num in arr1:
    while num > 0:
        prefixes_arr1.add(num)
        num = num // 10  # If num is 10, this adds 10, then divides by 10 to add 1


# --- 2. THE COMPARISON LOGIC ---
max_count = 0

# ERROR IN ORIGINAL: You used "for i in arr1: for j in arr2: if i == j:" 
# This only checked if full numbers from arr1 matched full numbers from arr2.
# SOLUTION: We loop through arr2, break each number down step-by-step, 
# and instantly check if that prefix exists in our arr1 prefix pool.
for num in arr2:
    while num > 0:
        if num in prefixes_arr1:
            
            # --- 3. COUNTING THE DIGITS ---
            # ERROR IN ORIGINAL: You did "while i != 0: i = i // 10". 
            # This directly destroyed your loop variable 'i', breaking the outer loops.
            # SOLUTION: We copy 'num' into a 'temp_num' variable so the main loop variable isn't damaged.
            max_val = 0
            temp_num = num  
            while temp_num != 0:
                temp_num = temp_num // 10
                max_val += 1
                
            if max_val > max_count:
                max_count = max_val
                
        num = num // 10  # Shrink the arr2 number (e.g., 17 becomes 1) to check the next prefix level

print("Longest Common Prefix Length:", max_count)








# =====================================================================
# YOUR ORIGINAL CODE DROPPED HERE FOR REFERENCE (Commented out):
# =====================================================================
# stra=""
# for s in arr2:
#     stra+=str(s)+" "
#
# a=""
# prefix=[]
# for i in range(len(stra)):  
#     if stra[i]!=" ":        
#         a+=stra[i]   
#         prefix.append(int(a))
#     else:
#         a=""                
#
# max_count=0
# for i in arr1:
#     for j in arr2:
#         if i==j:         <-- BUG 1: Checked for exact matches, missed partial prefixes (10 vs 17)
#             max=0
#             while i!=0:
#                 i=i//10  <-- BUG 2: Destroyed 'i', turning it to 0 and breaking next loops
#                 max+=1
#             if max>max_count:
#                 max_count=max