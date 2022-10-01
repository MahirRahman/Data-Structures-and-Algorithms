class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # f = defaultdict(dict)
        # vis = [0] * n
        # for s,d,c in flights:
        #     f[s][d] = c
        # heap = [(0,src,k+1)]
        # while heap:
        #     total, s, k = heapq.heappop(heap)
        #     if s == dst:
        #         return total
        #     if vis[s] != 0:
        #         continue
        #     vis[s] = k
        #     for inside_dic in f[s]:
        #         heapq.heappush(heap, (total+f[s][inside_dic], inside_dic, k - 1))            
        # return -1
        graph = collections.defaultdict(list)
        pq = []
        visited = [0] * n
        for u, v, w in flights:
            graph[u].append((w, v))

        heapq.heappush(pq, (0, k+1, src))
        while pq:
            price, stops, city = heapq.heappop(pq)

            if city is dst:
                return price
            if visited[city] >=stops:
                continue
            visited[city] = stops
            if stops>0:
                for price_to_nei, nei in graph[city]:
                    heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
        return -1