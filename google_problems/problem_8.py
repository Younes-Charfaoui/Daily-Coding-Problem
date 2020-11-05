"""This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting
node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space."""

from data_structure.linked_list import LinkedList, Element


# solution to the problem
def main(listOne, listTwo):
    """
    Main function.

    Args:
        listOne: (todo): write your description
        listTwo: (todo): write your description
    """
    l1 = listOne.print_list()
    l2 = listTwo.print_list()
    for i in l1:
        if i in l2:
            return i

    return None


listOne = LinkedList()
listTwo = LinkedList()

e1 = Element(99)
e2 = Element(1)
e3 = Element(8)
e4 = Element(10)

m1 = Element(3)
m2 = Element(7)
m3 = Element(8)
m4 = Element(10)

listOne.append(e1)
listOne.append(e2)
listOne.append(e3)
listOne.append(e4)

listTwo.append(m1)
listTwo.append(m2)
listTwo.append(m3)
listTwo.append(m4)

print(main(listOne,listTwo))