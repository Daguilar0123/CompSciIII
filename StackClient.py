from Stack import *

def main():
    stack1 = Stack()
    for i in range(10):
        stack1.push(i)
        print("Pushed: ", stack1.peek())

    print(stack1)
    print("\n")

    expression = input("Expression: ")
    print(is_valid_parentheses(expression))

    print("\n")

    infix_expr = input("Infix Expression: ")
    postfix_expr = infix_to_postfix(infix_expr)
    print(postfix_expr)

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

def infix_to_postfix(expression):
    precedence={"+":1,"-":1,"*":2,"/":2}
    output=[]
    stack2=Stack()

    tokens=expression.split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token =="(":
            stack2.push(token)
        elif token==")":
            while not stack2.isEmpty() and stack2.peek() != "(":
                output.append(stack2.pop())
            stack2.pop()
        else:
            while (not stack2.isEmpty() and stack2.peek() != "(" and
                   precedence.get(token,0)<=precedence.get(stack2.peek(),0)):
                output.append(stack2.pop())
            stack2.push(token)
    while not stack2.isEmpty():
        output.append(stack2.pop())
    return ''.join(output)
                

if __name__ == "__main__":
    main()