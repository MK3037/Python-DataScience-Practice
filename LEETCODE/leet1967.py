patterns = ["a","abc","bc","d"]
word = "abc"
count=0
for i in range(len(patterns)):
    if patterns[i] in word:
        count+=1
        
print(count)