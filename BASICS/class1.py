class maths:
    king='mihir'
    @staticmethod
    def add(num1,num2):
        return num1+num2
    
    def change(self,newking):              #passed object in self
        self.king=newking   #if i use king=newking then it will create a new variable and not global.
                            #in mentioned case also we are using instance variable and not changing class variable
                            #to change class variable we can use maths.king=newking
    @classmethod                           #passed class maths in self hence we can change class variable 
    def changeCompany(cls, newKing):      #here self is class.
        cls.king = newKing                  #can be used as alternative of constructor

s=maths()
print(s.add(2,3))           # Calling a static method using the instance
print(maths.add(1,2))       # Calling a static method using the class name
print(maths.king,'\n')

s.change('kurani')
print(s.king)               #instance variable changed
print(maths.king,'\n')      #class variable not changed

s.changeCompany("Tesla")  
print(maths.king)