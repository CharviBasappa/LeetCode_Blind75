##Floyd's Cycle Detection Algorithm (Tortoise and Hare)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

# Sample test cases
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]  # Creating a cycle
    
    return nodes[0]

# Test cases
solution = Solution()
# Example 1: Linked list with cycle
head1 = create_linked_list_with_cycle([3,2,0,-4], 1)
print(solution.hasCycle(head1))  # Output: True

# Example 2: Linked list with cycle
head2 = create_linked_list_with_cycle([1,2], 0)
print(solution.hasCycle(head2))  # Output: True

# Example 3: Linked list without cycle
head3 = create_linked_list_with_cycle([1], -1)
print(solution.hasCycle(head3))  # Output: False
