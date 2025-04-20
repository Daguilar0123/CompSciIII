from SimpleStack import *

def main():
    stack = Stack(10)
    print(stack)

    for word in ['May', 'the', 'force', 'be', 'with', 'you']:
        stack.push(word)

    print('After pushing', len(stack),
          'words on the stack, it contains: \n', stack)
    print('Is stack full?', stack.isFull())

    print('Popping items off the stack:')
    while not stack.isEmpty():
        print(stack.pop())

if __name__ == "__main__":
    main()