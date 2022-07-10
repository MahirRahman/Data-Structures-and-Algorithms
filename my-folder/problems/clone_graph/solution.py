"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        res = Node(1)
        queue = [(node, res)]
        visited = set()
        d = {}
        d[node] = res
        while queue:
            (curr, head) = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                neighbors = curr.neighbors
                for neighbor in neighbors:
                    # print(curr.val, neighbor.val)
                    newNode = None
                    if neighbor in d:
                        newNode = d[neighbor]
                    else:
                        newNode = Node(neighbor.val)
                        d[neighbor] = newNode
                    head.neighbors.append(newNode)
                    queue.append((neighbor, newNode))
                # print(head, head.neighbors)
        # print([neighbor.val for neighbor in res.neighbors])
        return res
                
                
            