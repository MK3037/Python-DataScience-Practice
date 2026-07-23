class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def get_time(self):
        # Taking input directly into the object attributes
        print("\nEnter hours:", end="")
        self.hour = int(input())
        print("Enter Minutes:", end="")
        self.minute = int(input())
        print("Enter Seconds:", end="")
        self.second = int(input())

    def print_time(self):
        # Displaying the stored time
        print(f"hour:{self.hour}")
        print(f"minute:{self.minute}")
        print(f"second:{self.second}")

    def add_time(self, x, y):
        # 1. Add everything up first
        self.second = x.second + y.second
        self.minute = x.minute + y.minute
        self.hour = x.hour + y.hour

        # 2. Handle seconds overflow
        if self.second >= 60:
            self.minute += self.second // 60  # Add the full minutes to the total
            self.second = self.second % 60    # Keep the remainder as seconds

        # 3. Handle minutes overflow
        if self.minute >= 60:
            self.hour += self.minute // 60    # Add the full hours to the total
            self.minute = self.minute % 60    # Keep the remainder as minutes

# Creating three objects as seen in the main() screenshot
t1 = Time()
t2 = Time()
t3 = Time()

# Getting and printing time for the first object
t1.get_time()
t1.print_time()

# Getting and printing time for the second object
t2.get_time()
t2.print_time()

# Adding t1 and t2, then storing the result in t3
t3.add_time(t1, t2)
print("after adding two objects", end="")
t3.print_time()