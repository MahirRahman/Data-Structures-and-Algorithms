class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        for i in range(len(prerequisites)):
                d[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()
        for key in d.keys():
            if key not in visited:
                if self.dfs(key, d, visited, []):
                    return False
        return True
        
            
            
    
    def dfs(self, i, d, visited, stk):
        if i in visited:
            if i in stk:
                return True
            else:
                return False
        visited.add(i)
        stk.append(i)
        for edge in d[i]:
            if self.dfs(edge, d, visited, stk):
                return True
        stk.pop()
        return False
        
                
            
        
        

