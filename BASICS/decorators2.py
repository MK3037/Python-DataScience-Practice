class employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # GETTER: This allows us to access email as an attribute (x.email)
    # Why: If first or last changes, email updates automatically. 
    # Without this, email would stay stuck with the original names.
    @property
    def email(self):
        return self.first + "." + self.last + "@email.com"

    # GETTER: Allows us to treat the fullname method like a simple variable.
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # SETTER: This is triggered when we try to assign a value to fullname.
    # Why: It allows us to update 'first' and 'last' name at the same 
    # time by just providing one full string.
    @fullname.setter                             
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # DELETER: This is triggered when we use 'del x.fullname'.
    # Why: It allows you to run "cleanup" code (like setting values to None)
    # when an attribute is deleted.
    @fullname.deleter                         
    def fullname(self):
        print("deleted!")
        self.first = None
        self.last = None

# --- Testing the Class ---

x = employee('mihir', 'kurani')

# 1. Test Getter/Property: Change first name and see if email follows
x.first = 'purvesh'
print(x.email)    # Result: purvesh.kurani@email.com

# 2. Test Setter: Setting fullname updates first and last name automatically
x.fullname = "mihir kurani"
print(x.first)    # Result: mihir
print(x.last)     # Result: kurani

# 3. Test Deleter: Clean up the object
del x.fullname    # Result: Prints "deleted!"
print(x.first)    # Result: None