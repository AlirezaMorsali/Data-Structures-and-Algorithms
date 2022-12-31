"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


# Naive method: traverse the linked list and add nodes to a `set` and on each node check if it exists.
# O(N) memnory O(N) time

# We want O(1) memory
# Floyd's tortoise and hare algorithm
# Fast-Slow pointers

def hasCycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detectCycle(head):
    slow = fast = head
    meet = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    while head != slow:
        head = head.next
        slow = slow.next
    return slow
