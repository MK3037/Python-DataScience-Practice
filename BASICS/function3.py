#CLOSSER
def func1():
    def func2():
        print("hi")
    return func2            #if no '()' in return then we have to make a object while calling this function
x=func1()
x()


def func3():
    def func4():
        print("hi")
    return func4()          #if '(())' then we can directly call this function
func3()


def hi():
    print("yo")
hi()
x=hi()
