def factorial(n):
    if n == 1:
        return 1 
    return n * factorial(n-1)

if __name__ == "__main__":
    print("Factorial is ",factorial(4))

'''Recursion doesn’t solve the problem immediately — it postpones work until the base case, then solves everything backward.'''