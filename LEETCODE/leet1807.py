def evaluate(s, knowledge):
        knowledge=dict(knowledge)
        ans=[]
        found=False
        word=[]
        for i in range(len(s)):
            if s[i]==')':
                found=False
                ans.append(knowledge.get("".join(word[1:]),'?'))
                word=[]
            elif s[i]=='(' or found==True:
                found=True
                word.append(s[i])
            else:
                ans.append(s[i])
        return "".join(ans)

s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(evaluate(s,knowledge))