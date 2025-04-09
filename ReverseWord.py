from SimpleStack import *

stack = Stack(100)              # Create a stack to hold letters

word = input("Word to reverse: ")

for letter in word:             # Loop over letters in word
    if not stack.isFull():
        stack.push(letter)

reverse = ''                    # Build the reversed version
while not stack.isEmpty():      # by popping the stack until empty
    reverse += stack.pop()

print('The reverse of', word, 'is', reverse)