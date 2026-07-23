def my_decorator(func):     #2. my_decorator(say_hello)
    def wrapper():          #3. new function wrapper as follow:
        print("Something is happening before the function is called.")
        func()              #4. say_hello initalized
        print("Something is happening after the function is called.")
    return wrapper          #5. modified new function returned

@my_decorator
def say_hello():            #1. thats say_hello passed as func in my_decorator
    print("Hello!")

say_hello()                 #0. say_hello called