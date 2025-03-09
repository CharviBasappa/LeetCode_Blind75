from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Sample Test Cases
solution = Solution()

print("\nRecursive Approach:")
head = create_linked_list([1,2,3,4,5])
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: [5, 4, 3, 2, 1]

head = create_linked_list([1,2])
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: [2, 1]

head = create_linked_list([])
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: []