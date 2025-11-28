# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to merge two sorted linked lists
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists and append the smaller node to current
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If any nodes are left in list1 or list2, append them
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    # Return the merged list starting from dummy.next
    return dummy.next

# Helper function to print linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


list1 = ListNode(1, ListNode(3, ListNode(5)))


list2 = ListNode(2, ListNode(4, ListNode(6)))


merged_head = mergeTwoLists(list1, list2)

printList(merged_head)
