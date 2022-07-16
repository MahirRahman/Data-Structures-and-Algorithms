class Solution:
    # -1 in visited
    # 1 in current path
    # unvisited
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i : [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            d[pre_req].append(course)
        color = [0] * numCourses
        final_result = []
        def dfs(course):
            if color[course] == -1:
                return True
            if color[course] == 1:
                return False
            color[course] = -1
            for next_course in d[course]:
                if dfs(next_course):
                    return True
            color[course] = 1
            final_result.append(course)
            return False
        for key in d.keys():
            if color[key] != -1:
                if dfs(key):
                    return []
        return final_result[::-1]
                