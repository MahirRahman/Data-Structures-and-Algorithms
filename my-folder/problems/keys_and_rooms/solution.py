class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = [0]
        while queue:
            r = queue.pop(0)            
            for i in rooms[r]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                
        return len(visited) == len(rooms)
        