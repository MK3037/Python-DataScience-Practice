class Employee:
    companyName = "Apple"  # Class Variable     serve same as static variable
    noOfEmployees = 0      # Class Variable

    def __init__(self, name):
        self.name = name                # Instance Variable
        self.raise_amount = 0.02         # Instance Variable
        Employee.noOfEmployees += 1     # Increment class variable on each instance creation

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Creating instances
emp1 = Employee("Harry")
emp1.raise_amount = 0.3          # Changing instance variable for emp1
emp1.companyName = "Apple India"  # This creates an instance variable for emp1
emp1.showDetails()

Employee.companyName = "Google"   # Changing the class variable for all instances
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"       # This creates an instance variable for emp2
emp2.showDetails()