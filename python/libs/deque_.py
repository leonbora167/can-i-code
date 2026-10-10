from collections import deque

elements = ["apple", "banana", "rabbit", "cat", "ball"]

ds = deque(elements)
print(ds)

ds.append("bat") #like list add at end 
print(ds)

ds.appendleft("fish") #append at beginning - left side
print(ds)

ds.extend(["star", "moon", "hail"]) #unpacks iterable and adds them one by one
print(ds)

ds.extendleft(["loaf", "car"]) #Same but from left side -- although I can see that the elements are being added from the right side of iterable
print(ds)

print(ds.pop()) #Removes returns last element

print(ds.popleft()) # Removes fikrst elemnent

ds.rotate(-2) #Rotates element from left side 
print(ds)

ds.rotate(3) #rotates by n elements from right side
print(ds)