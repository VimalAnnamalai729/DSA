class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Creating list2: [1, 3, 4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merge_two_lists(list1, list2)