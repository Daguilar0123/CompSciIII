from Stack import *

def main():
    stack1 = Stack()
    for i in range(6):
        stack1.push(i)
        print("Pushed: ", stack1.peek())

    print(stack1)

if __name__ == "__main__":
    main()