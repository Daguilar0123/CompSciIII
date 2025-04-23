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

if __name__=="__main__":
    main()