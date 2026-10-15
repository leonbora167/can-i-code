'''
def func1():
    something

def func2():
    something

Now these two functions are doing something

What does 

@func1
def func2():
    pass
    
DO ? -> Tells python that the base function func2() must be enhanced by the decorator func1() before it is used

There is something called "Single responsbility" in programming
Implying each function should perform one single task only

def brew_tea():
    start = time.time()
    print("Brew started")
    time.sleep(1)
    print("Brew over")
    print("Time taken is ",time.time()-start)

def brew_match():
    start = time.time()
    print("Brew match started")
    time.sleep(1)
    print("Match brew over")
    print("Time taken is ", time.time()-start)

We can see here for these functions to calculate the time taken to start and complete these functions there is one functionality
a.k.a time caluclation which is being repeated, 
To prevent code from building up with repeated code and also to adhere to single responsbility principle we use decorators
'''

import time

def brew_tea():
    print("Brew started")
    time.sleep(1)
    print("Brew Over")
#We are not adding anything for time calculation

def enhancer_function(base_func):
    def calculate_time():
        start = time.time()
        base_func()
        print("Time taken is ", time.time()-start)
    return calculate_time

'''
From what i infer
enhancer function parameter is the function being sent to it, which needs to use some other feature of another function
calculate_time() calculates the start time, calls the function which is being sent to it then calculates the end time
Which is the execution time of the function being sent to it
'''

#Way 1 -- Separates the decoration from the function definition, making it less obvious while reading the code
decorator_variable = enhancer_function(brew_tea)
decorator_variable()

#Way 2
@enhancer_function
def brew_match():
    print("Brew matcha started")
    time.sleep(2)
    print("Match brew over")

brew_match()

'''
What if u pass brew_tea("23", "a")
it ll throw an error since using a decorator means enhancing brew_tea() with enhancer_function() before it is called
so enhancer_function() is called first 
We have to modify the decorator to accept the arguments, but it ll then break for those functions which are using the decorator but without any argument/parameter
In this case you have to use *args, but also **kwargs to accept any number of parameters or dictionary of parameters
To return a value from the function using the decorator, the decorator itself has to return the value within it
'''

def enhancer_function(base_func): #decorator
    def calculate_time(*args, **kwargs): #Wrapper
        start = time.time()
        response = base_func(*args, **kwargs)
        print("Time taken is ", time.time()-start)
        return response
    return calculate_time

@enhancer_function
def brew_tea(a, b):
    print("Brew started")
    time.sleep(1)
    print("Brew Over" + a + b)

@enhancer_function
def brew_match():
    print("Brew matcha started")
    time.sleep(2)
    print("Match brew over")
    return "Testing for brew mathca"

brew_tea("test1", "test2")
a = brew_match
print(a)

'''
Gemini assisted study

When you use the @enhancer_function syntax, Python fundamentally replaces your original brew_tea function with the calculate_time wrapper function.

two or more wrappers inside a decorator ?
Yes, absolutely. Because Python treats functions as first-class objects, you can define as many functions inside the decorator as you need.
You might do this if your wrapper needs to rely on a complex helper function, but you want to keep that helper hidden from the global scope. 
The only strict requirement of a standard decorator is that it ultimately returns a single callable function to replace the base function.

def complex_decorator(base_func):
    # Helper function 1 (hidden from the outside)
    def validate_input(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError("All arguments must be strings!")

    # Helper function 2 (hidden from the outside)
    def log_event():
        print("Logging this execution to a file...")

    # The actual wrapper function that uses the helpers
    def wrapper(*args, **kwargs):
        validate_input(*args)
        log_event()
        return base_func(*args, **kwargs)
    
    # We still only return the single wrapper
    return wrapper

@complex_decorator
def greet(name):
    return f"Hello, {name}"
'''

#so one decorator has multiple wrappers, but they will all be used by the one callable function within it which would replace the 
#base function(one using the decorator)