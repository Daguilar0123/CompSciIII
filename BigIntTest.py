"""
BigIntTest.py

Purpose:
    Demonstrates Python integer identity behavior and the small-integer cache.
    It prints object IDs for small ints (within cache) and large ints (beyond cache)
    and compares object identity (is) for each case.
"""

# Test identity for small integers within the pre-allocated cache (-5 to 256)
a = 100
b = 100
print(id(a))
print(id(b))

aISb = a is b  # True because 100 is cached
print(aISb)

# Test identity for the upper bound of the cache (256)
x = 256
y = 256
print(id(y))
print(id(x))
xISy = x is y  # True because 256 is still in cache
print(xISy)

# Test identity for integers beyond the small-integer cache
z = 2**32
w = 2**32
print(id(z))
print(id(w))
zISw = z is w  # May be True due to compiler constant folding, but runtime identity can differ
print(zISw)

print()  # End of BigIntTest: blank line for readability