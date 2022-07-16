class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lst = []
        d = {i :[] for i in range(numCourses)}
        degree = [0] * numCourses
        for i,j in prerequisites:
            d[i].append(j)
            degree[j] += 1
        queue = collections.deque([index for index, i in enumerate(degree) if i == 0])
        while queue:
            node = queue.popleft()
            for edge in d[node]:
                degree[edge] -= 1
                if degree[edge] == 0:
                    queue.append(edge)
        return sum(degree) == 0