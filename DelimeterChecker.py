from SimpleStack import *

stack = Stack(100)          # Create a stack to hold delimeter tokens

expr = input("Expression to check: ")

errors = 0          # Assume no errors in expression

for pos, letter in enumerate(expr):     # Loop over letters in expression
    if letter in "{[(":         # Look for starting delimeter
        if stack.isFull():      # A full stack means we can't continue
            raise Exception('Stack overflow on expression')
        else:
            stack.push(letter)  # Put left delimiter on stack

    elif letter in "}])":       # Look for closing delimeter
        if stack.isEmpty():     # If stack is empty, no left delimiter
            print("Error:", letter, "at position", pos,
                  "has no matching left delimiter")
            errors += 1
        else:
            left = stack.pop()  # Get left delimiter from stack
            if not (left == "{" and letter == "}" or
                    left == "[" and letter == "]" or
                    left == "(" and letter == ")"):
                print("Errors:", letter, "at position", pos,
                      "does not match left delimiter", left)
                errors += 1

# After going through entire expression, check if stack empty
if stack.isEmpty() and errors == 0:
    print("Delimiters balance in expression", expr)

elif not stack.isEmpty():       # Any delimiters on stack weren't matched
    print("Expression missing right delimiters for", stack)