import Array

maxSize = int(input("Enter the maximum size for your array: "))

arr = Array.Array(maxSize)

print(len(arr))
for x in arr:
    print(x)
    
arr.traverse()