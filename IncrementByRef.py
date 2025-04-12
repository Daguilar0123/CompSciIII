def increment(a, b):
    a +=1
    b[0] += 1

x = 1
y = [1]
increment(x,y)
print(x, y)