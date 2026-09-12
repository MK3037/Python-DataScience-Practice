s = "the sky is blue"

s_list = s.split()

for i in range(len(s_list)//2):
    s_list[i],s_list[len(s_list)-1-i]=s_list[len(s_list)-1-i],s_list[i]

s = " ".join(s_list)

print(s) 