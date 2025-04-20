def increment(a, b):
    a +=1
    b[0] += 1

x = 1
y = [1]
increment(x,y)
print(x, y)

def append_item(lst, item):
    # Modifies the list by appending a new item.
    lst.append(item)

numbers = [1, 2, 3]
append_item(numbers, 4)
print("After append_item:", numbers)  # Output: [1, 2, 3, 4]

def reassign_list(lst):
    # This rebinds the local variable lst to a new list,
    # but it does not modify the original list.
    lst = [4, 5, 6]
    return lst

original_list = [1, 2, 3]
new_list = reassign_list(original_list)
print("Original list after reassign_list:", original_list)  # Output: [1, 2, 3]
print("New list:", new_list)