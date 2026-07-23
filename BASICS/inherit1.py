#MULTLEVEL
class Animal:
    def show(self):
        print("animal")

class Cat(Animal):
    def show(self):
        print("cat")

class RussianCat(Cat):
    def show(self):
        print("russian cat")

if __name__ == "__main__":
    r = RussianCat()
    
    # Accessing methods from specific levels of the hierarchy
    Animal.show(r)      # Equivalent to r.animal::show()
    Cat.show(r)         # Equivalent to r.cat::show()
    r.show()            # Calls the local (RussianCat) show method
    
    print("-" * 10)
    
    a = Cat()
    a.show()            # Outputs: cat
    
    k = Animal()
    k.show()            # Outputs: animal