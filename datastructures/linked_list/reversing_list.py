
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def print_node(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" --> ")
        curr = curr.next
    print()

node1 = ListNode(0)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)

# Update node1 with the new head after reversing the linked list
node1 = reverse(node1)

print_node(node1)
