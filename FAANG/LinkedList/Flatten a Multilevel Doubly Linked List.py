# """
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
head = Node(1,)
n2 = Node(2, prev=head)
head.next = n2
n3 = Node(3, prev=n2)
n2.next = n3
n4 = Node(4, prev=n3)
n3.next = n4
n5 = Node(5, prev=n4)
n4.next = n5
n6 = Node(6, prev=n5)
n5.next = n6
n7 = Node(7)
n3.child = n7
n8 = Node(8, prev=n7)
n7.next = n8
n9 = Node(9, prev=n8)
n8.next = n9
n10 = Node(10, prev=n9)
n9.next = n10
n11 = Node(11)
n8.child = n11
n12 = Node(12, prev=n11)
n11.next = n12

# Bottom up flattening
# Alternatively for each node if there is a child,
# we find the tail of that linked list and don't worry about children of that linkedlist
# flatten the child list and then go to the next node


def flatten(head):
    if not head:
        return head

    def flat(node):
        if node.child:
            if node.next:
                child = node.child
                next = node.next
                last_child = flat(node.child)
                last_child.next = node.next
                node.next.prev = last_child
                node.next = child
                child.prev = node
                node.child = None
                return flat(next)
            else:
                last_child = flat(node.child)
                node.next = node.child
                node.child.prev = node
                node.child = None
                return last_child
        else:
            if node.next:
                return flat(node.next)
            else:
                return node
    flat(head)
    return head


flatten(head)
