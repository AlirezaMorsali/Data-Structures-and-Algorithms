class Node():
    def __init__(self, value, next=None) -> None:
        self.val = value
        self.next = next

    @staticmethod
    def to_list(head):
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals

    @staticmethod
    def from_list(l: list):
        head = Node(l[0])
        node = head
        for val in l[1:]:
            node.next = Node(val)
            node = node.next
        return head


def reverse(head):
    def rec_rev(prev, current):
        if current is None:
            return prev
        else:
            next = current.next
            current.next = prev
            return rec_rev(current, next)

    return rec_rev(None, head)


def reverse_from_to(head, left, right):
    """
    Reverse the linked list from node n<m to m
    """
    # Goto n
    # Reverse n to m
    # link
    assert 1 <= left <= right
    index = 1
    current = head
    prev = None
    start = None
    while index <= right:
        if index < left:
            if index == left-1:
                start = current
            prev = current
            current = current.next
        else:
            if index == right:
                end = current.next
            next = current.next
            current.next = prev
            prev = current
            current = next
        index += 1

    if start:
        start.next.next = end
        start.next = prev
    else:
        head.next = end
        head = prev
        # start.next = next

    return head
    # def rec_rev(prev, current, left_node, right_node, index):
    #     if current is None:
    #         return
    #     if index <= left:
    #         if index == left-1:
    #             left_node = current
    #         next = current.next
    #     elif index > left and index < right:
    #         next = current.next
    #         current.next = prev
    #     else:
    #         right_node = current.next
    #         current.next = prev
    #         start = left_node.next
    #         left_node.next = current
    #         start.next = right_node
    #         return
    #     index += 1
    #     return rec_rev(current, next, left_node, right_node, index)
    # rec_rev(None, head, 0, 0, 1)


# head = Node.from_list([1, 2, 3, 4, 5, 6])
# print(Node.to_list(head))

# print("Revere")
# head = reverse(head)
# print(Node.to_list(head))

# print("Revere from 2 to 5")
# head = reverse_from_to(head, 2, 5)
# print(Node.to_list(head))

head = Node.from_list([5])
print(Node.to_list(head))
print("Revere from 1 to 1")
head = reverse_from_to(head, 1, 1)
print(Node.to_list(head))

head = Node.from_list([5, 3])
print(Node.to_list(head))
print("Revere from 1 to 2")
head = reverse_from_to(head, 1, 2)
print(Node.to_list(head))

head = Node.from_list([1, 2, 3, 4, 5, 6, 7, 8])
print(Node.to_list(head))
print("Revere from 1 to 2")
head = reverse_from_to(head, 2, 5)
print(Node.to_list(head))
