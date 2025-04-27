from LinkedList import *

def main():
    ll = LinkedList()

    ll.getFirst()

    ll.insert("First Element")
    ll.insert("Second Element")
    ll.insert("Third Element")


    print(ll)
    print(ll.first())
    ll.insertAfter("Third Element", "2a")
    print(ll)
    ll.delete("First Element")
    print(ll)

    ll2 = LinkedList()
    x=int(input("How many items do you want to insert? "))
    for i in range(x):
        ll2.insert(input("Enter the first element: "))
    print(ll2)
    if x >=2 and x % 2 == 0:
        print(ll2.delete(str(x-2)))
    elif x>=1 and x % 2 != 0:
        print(ll2.delete(str(x-1)))
    print(ll2)
    found = ll2.find(input("Enter the element you want to find: " ))
    print(found)

if __name__=="__main__":
    main()