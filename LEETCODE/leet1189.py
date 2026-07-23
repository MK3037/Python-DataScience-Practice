def maxNumberOfBalloons(text):
        hash={}
        for i in text:
            hash[i]=hash.get(i,0)+1
        hash['l']=hash.get('l',1)//2
        hash['o']=hash.get('o',1)//2

        return min(hash.get(i,0) for i in 'balon')

a=maxNumberOfBalloons('nlaebolko')
print(a)