"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_nodes = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current=queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])

        return cloned_nodes[node]
        
# Helper function to build a graph from an adjacency list
def build_graph(adjList):
    if not adjList:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}
    
    for i, neighbors in enumerate(adjList):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    
    return nodes[1]

# Helper function to convert graph to adjacency list for output
def graph_to_adj_list(node):
    if not node:
        return []

    visited = {}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        if curr.val not in visited:
            visited[curr.val] = [neighbor.val for neighbor in curr.neighbors]
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    return [visited[i] for i in sorted(visited.keys())]

# Function to test cloneGraph and print results
def test_clone_graph(adjList, expected):
    input_node = build_graph(adjList)
    solution = Solution()
    cloned_graph = solution.cloneGraph(input_node)
    output = graph_to_adj_list(cloned_graph)
    
    print(f"Input: {adjList}")
    print(f"Expected Output: {expected}")
    print(f"Actual Output: {output}")
    print(f"Test {'PASSED' if output == expected else 'FAILED'}\n")

# Run test cases when script is executed
if __name__ == "__main__":
    print("Running Test Cases for cloneGraph...\n")
    
    # 1. Basic Graph
    test_clone_graph([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]])

    # 2. Single Node
    test_clone_graph([[]], [[]])

    # 3. Empty Graph
    test_clone_graph([], [])

    # 4. Linear Graph
    test_clone_graph([[2],[1,3],[2,4],[3]], [[2],[1,3],[2,4],[3]])

    # 5. Star Graph
    test_clone_graph([[2,3,4],[1],[1],[1]], [[2,3,4],[1],[1],[1]])