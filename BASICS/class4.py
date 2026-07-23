class Complex:
    def __init__(self):
        # Initializing real and imaginary parts
        self.real = 0
        self.imag = 0

    def read_data(self):
        print("Enter real and imaginary number:", end=" ")
        # Using split() to take two numbers on one line like C++ cin >> real >> imag
        data = input().split()
        self.real = int(data[0])
        self.imag = int(data[1])

    def add_complex_numbers(self, comp1, comp2):
        # Create a 'temp' instance to hold the result
        temp = Complex()
        temp.real = comp1.real + comp2.real
        temp.imag = comp1.imag + comp2.imag
        # Returning the object back to the caller
        return temp

    def display_sum(self):
        print(f"Sum = {self.real}+{self.imag}i")

c1,c2,c3 = Complex(),Complex(),Complex()


c1.read_data()
c2.read_data()

ans = c3.add_complex_numbers(c1, c2)
ans.display_sum()