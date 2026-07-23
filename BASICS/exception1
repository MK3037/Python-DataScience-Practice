def func1():
    try:
        num = int(input("Enter an index: "))
        a = [6, 3]
        print(a[num])
        return 1  
    except ValueError:
        print("Number entered is not an integer.")
        return 0 
    except IndexError:
        print("Index Error: The index is out of range.")
        return 0  
    
    finally:
        # This code ALWAYS runs, even after a 'return' statement 
        print("I am always executed (Cleanup code)")


x = func1()
print(f"Function returned: {x}")