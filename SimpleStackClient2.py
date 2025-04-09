from SimpleStack import *

#!/usr/bin/env python3

def main():
    # create a new stack instance (assuming the class is named 'Stack')
    maxSize = 20
    stack = Stack(maxSize)
    print("Created a new stack.")

    # Push some values onto the stack
    for i in range(maxSize):
        print(f"Pushing {i} onto the stack.")
        stack.push(i)

    # Display the current state of the stack (implementation dependent)
    print("Current stack:", stack)

    # Peek at the top value without removing it
    top_value = stack.peek()
    print(f"Top value (peek): {top_value}")

    # Pop the top value from the stack
    popped_value = stack.pop()
    print(f"Popped value: {popped_value}")
    print("Stack after pop:", stack)

    # Empty the stack completely
    print("Emptying the stack:")
    while not stack.isEmpty():
        print(f"Popped: {stack.pop()}")
    
    print("Stack is now empty.")

if __name__ == "__main__":
    main()