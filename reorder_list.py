from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Sample Test cases

# Test Case 1
head1 = list_to_linked_list([1, 2, 3, 4])
Solution().reorderList(head1)
print(linked_list_to_list(head1))  # Output: [1, 4, 2, 3]

# Test Case 2
head2 = list_to_linked_list([1, 2, 3, 4, 5])
Solution().reorderList(head2)
print(linked_list_to_list(head2))  # Output: [1, 5, 2, 4, 3]

# Test Case 3 (Single Node)
head3 = list_to_linked_list([1])
Solution().reorderList(head3)
print(linked_list_to_list(head3))  # Output: [1]

# Test Case 4 (Two Nodes)
head4 = list_to_linked_list([1, 2])
Solution().reorderList(head4)
print(linked_list_to_list(head4))  # Output: [1, 2]

# Test Case 5 (Edge Case: Even Number of Elements)
head5 = list_to_linked_list([10, 20, 30, 40, 50, 60])
Solution().reorderList(head5)
print(linked_list_to_list(head5))  # Output: [10, 60, 20, 50, 30, 40]
