class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes = {content[0]:content[1] for content in paths}
        k = paths[0][0]
        while True:
            if routes.get(k) == None:
                return k
            k = routes[k]