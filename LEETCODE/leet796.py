def rotateString(s, goal):
        if len(s) != len(goal):
            return False
        
        return goal in (s + s)

s = "abcde"
goal = "cdeab"
x=rotateString(s,goal)
print(x)