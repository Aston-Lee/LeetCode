class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        # try dq
        adj = defaultdict(list)
        for start, end, price in flights:
            adj[start].append([price, end])
            
        res = float('inf')
        dq = deque()
        stops = 0
        for price, station in adj[src]:
            if station == dst:
                res = min(res, price)
            else:
                dq.append([price, station])
        adj[src] = []
        
        visited = defaultdict(int)
        
        while dq and stops < k:
            stops += 1
            for _ in range(len(dq)):
                price, end = dq.popleft()
                for add_price, end_station in adj[end]:
                    new_price = price + add_price 
                    if end_station == dst:
                        res = min(res, new_price)
                    else:
                        if end_station in visited and  visited[end_station] < new_price:
                            continue
                        else:
                            dq.append([new_price, end_station])
                            visited[end_station] = new_price
                        
        return res if res != float('inf') else -1
        
            