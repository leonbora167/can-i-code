def fibonacci(n, dps): # Memoization - Top Down approach = (n -> 0) 
    if n <= 1:
        return n
    if dps[n] != -1:
        return dps[n]
    dps[n] = fibonacci(n-1, dps) + fibonacci(n-2, dps) 
    return dps[n]

n = 7
dps = [-1] * (n+1) # To go from 0 to index 'n'
print(fibonacci(n, dps))


def fibonacci(n): # Tabulation - Iterative - Forward approach (0 -> n)
    dps = [0] * (n+1)
    
    dps[0] = 0
    dps[1] = 1 

    for i in range(2, n+1):
        dps[i] = dps[i-1] + dps[i-2]
    
    return(dps[n])

print(fibonacci(7))


def step(n): # How many 1 step or 2 step combinations possible to reach n steps ?
    '''1 step has 1 combination 
    2 step has 2 combinations (1+1, 2)
    similary 3 step has 3 combinations (1+1+1, 1+2, 2+1)
    
    Therefore f(1) = 1
              f(2) = 2
              f(3) = f(2) + f(1)
              f(n) = f(n-1) + f(n-2)'''
    
    lis = [0] * (n+1) #empty 0's array from index 0 to n 
    lis[1] = 1
    lis[2] = 2 

    for i in range(3, n+1):
        lis[i] = lis[i-1] + lis[i-2]
    return lis[n]

print(step(4))

def rob(nums): #Provided you are given a list of houses you can rob, whats teh maximum u can rob without touching adjacent ones 
    dp = [0] * len(nums) 

    #Add corner cases for 0 and 1 in leetcode

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[n-1]