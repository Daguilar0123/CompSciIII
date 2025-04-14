def weightedsum(values, weights, missing=0):
    sum = 0
    for i, val in enumerate(values):
        sum += val * (weights[i] if i < len(weights) else missing)
    return sum    
    
result1 = weightedsum([4, 9, 16, 25], [2, 2])
result2 = weightedsum([4, 9, 16, 25], [2, 2], 1)
result3 = weightedsum([1, 1, 1, 1, 1],[1,1])

print(result1)
print(result2)
print(result3)