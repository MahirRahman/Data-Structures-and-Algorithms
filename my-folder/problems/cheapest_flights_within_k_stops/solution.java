class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        HashMap<Integer,HashMap<Integer,Integer>> f = new HashMap<>();
    	for (int[] flight: flights) {
            if (!f.containsKey(flight[0])) f.put(flight[0], new HashMap<>());
            f.get(flight[0]).put(flight[1],flight[2]);
    		// HashMap<Integer,Integer> details = f.getOrDefault(flight[0], new HashMap<>());
    		// details.put(flight[1], flight[2]);
    	// Set up priority queue
    	}
    	int[] visited = new int[n];
    	Arrays.fill(visited, 0);
    	PriorityQueue<int[]> q= new PriorityQueue<>((a,b) -> (Integer.compare(a[0], b[0])));
    	q.offer(new int[]{0,src,k+1});
    	while (q.isEmpty() == false) {
    		int[] stop = q.poll();
            int price = stop[0];
            int city = stop[1];
            int stops = stop[2];
    		if (city == dst) {
    			return price;
    		}
    		if (visited[city] >= stops) {
    			continue;
    		}
            visited[city] = stops;
    		if (stops > 0) {
	    		HashMap<Integer,Integer> nextStop = f.getOrDefault(city, new HashMap<>());
	    		for (int key: nextStop.keySet()) {
	    			int newCost = nextStop.get(key);
	    			q.offer(new int[] {price+newCost,key,stops-1});
	    		}
    		}
    	}
    		
    		
    	return -1;
    }
}