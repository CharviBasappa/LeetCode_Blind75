# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Sample Test Cases
solution = Solution()

# Test Case 1
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_head = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4]

# Test Case 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged_head = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_head))  # Output: []

# Test Case 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged_head = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_head))  # Output: [0]
