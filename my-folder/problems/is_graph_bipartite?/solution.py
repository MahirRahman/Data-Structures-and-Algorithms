# 0 for not visited
# 1 for blue
# -1 for red
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        for i in range(len(graph)):
            if color[i] == 0 and self.fillColor(color, graph, 1, i) is False:
                return False
        return True
    
    def fillColor(self, color, graph, c, i):
        if color[i] != 0:
            return color[i] == c
        color[i] = c
        for j in graph[i]:
            if self.fillColor(color, graph, -c, j) is False:
                return False
        return True
    
        # print(red)
        # print(blue)
                    