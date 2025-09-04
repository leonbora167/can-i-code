a = 5
b = a 

print("Location of a is ", id(a))
print("Location of b is ", id(b))

print("Value of a is ", a)
print("Value of b is ", b)
# Both locations ll be the same, since b is pointing to a. It has the same value as a
# Compiler creates the integer value 5 in a location that is being referred to by a and in turn by b 

b = 3

print("Updated Location of a is ", id(a))
print("Updated Location of b is ", id(b))

print("Updated Value of a is ", a)
print("Updated Value of b is ", b)
# Location of a remains the same but on updating the value of b we see that the location of b changes
# In Python integers are immutable. Such that they cannot be modified. So on changing the value at "b"
# The compiler makes a new memory location for 3 and assigns that memory to b and removes it from referencing a

a = {"data" : 2}
b = a

print("Location of a is ", id(a))
print("Location of b is ", id(b))

print("Value of a is ", a)
print("Value of b is ", b)
#Similarly like above a and b refer to same location

b["data"] = 10

print("Updated Location of a is ", id(a))
print("Updated Location of b is ", id(b))

print("Updated Value of a is ", a)
print("Updated Value of b is ", b)
# Now both a and b have their values updated to "data" : 10
# Dictionaries in Python are mutable so the values can change will keeping the location same

c = {"data" : 20}
b = c 
print("Updated Location of b is ", id(b))
print("Updated Location of c is ", id(c))

print("Updated Value of b is ", b)
print("Updated Value of c is ", c)
#Now b points to the new location of c while a points to nothing
# a = b makes it point to b which is pointing to c
a = b 

print("Value of a is", a)
print("Location of a is ",id(a))
# The original value of a is now not being pointed by any variable
# Compiler takes care of it by deleting it from memory -> Garbage collection