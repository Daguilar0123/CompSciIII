from DoubleEndedList import *

def second(x): return x[1]              # return value at second index in zero-indexed list

dlist = DoubleEndedList()

print('Initial list has', len(dlist), 'element(s) and empty =',
      dlist.isEmpty())
after = None
people = ['Raj', 'Amir', 'Adi', 'Don', 'Ken', 'Ivan']
for i, person in enumerate(people):
    if after:
        dlist.insertAfter(after, (i * i, person), key=second)
    else:
        dlist.insert((i * i, person))
        after = person
print('After inserting', len(dlist) - 1,
      'persons into the linked list after,', after, 'it contains:')
dlist.traverse()
print('First:', dlist.first(), 'and Last:', dlist.last())