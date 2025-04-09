from Stack import *

def main():
    stack1 = Stack()
    for i in range(10):
        stack1.push(i)
        print("Pushed: ", stack1.peek())

    print(stack1)
    print("\n")

    expression="({}[])"
    print(is_valid_parentheses(expression))

def is_valid_parentheses(expression):
    stack=Stack()
    pairs={")":"(","}":"{","]":"["}
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.isEmpty() or stack.peek() !=pairs[char]:
                return False
            stack.pop()
    return stack.isEmpty()


if __name__ == "__main__":
    main()