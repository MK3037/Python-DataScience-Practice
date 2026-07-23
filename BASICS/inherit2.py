#MULTIPLE
class First:
    def __init__(self):
        # first sum s is created and instantly it goes to first
        # mentioned base class 'first' and hence its constructor is invoked.
        self.a = int(input("enter first element: "))

class Second:
    def __init__(self):
        # Then it goes to second base class 'second'
        # and hence its constructor is invoked.
        self.b = int(input("enter second element: "))

class Sum(First, Second):
    def __init__(self):
        # Explicitly calling parent constructors to mimic C++ and java behavior, in python parent cons. arent called automatically
        First.__init__(self)
        Second.__init__(self)
        
        # And finally the derived class is created and hence it invoked.
        self.c = self.a + self.b
        print(f"result is: {self.c}")

# Main execution
if __name__ == "__main__":
    s = Sum()
    print(s.c)
    # DESTRUCTION WOULD OCCUR IN REVERSE ORDER for this.