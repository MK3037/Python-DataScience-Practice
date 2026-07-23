class Distance:
    def __init__(self, meters):
        # Basic to Class: Initialize object state
        self.meters = float(meters)
        print(f"Object created with {self.meters} meters.")

    # Class to Basic: Convert to int
    def __int__(self):
        return int(self.meters)

    # Class to Basic: Convert to string
    def __str__(self):
        return f"{self.meters}m"

    # Operator Overloading: Use + operator
    def __add__(self, other):
        return Distance(self.meters + other.meters)

    # Destructor: Cleanup when object is destroyed
    def __del__(self):
        print(f"Object with {self.meters} meters is being destroyed.")

# Usage
d1 = Distance(10)
d2 = Distance(20.5)
d3 = d1 + d2

print(f"Result as string: {str(d3)}")
print(f"Result as integer: {int(d3)}")

# The __del__ method will be called when these objects are no longer referenced