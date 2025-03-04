from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy  

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

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
head = create_linked_list([1, 2, 3, 4, 5])
n = 2
print(linked_list_to_list(solution.removeNthFromEnd(head, n)))  # Output: [1, 2, 3, 5]

# Test Case 2
head = create_linked_list([1])
n = 1
print(linked_list_to_list(solution.removeNthFromEnd(head, n)))  # Output: []

# Test Case 3
head = create_linked_list([1, 2])
n = 1
print(linked_list_to_list(solution.removeNthFromEnd(head, n)))  # Output: [1]
