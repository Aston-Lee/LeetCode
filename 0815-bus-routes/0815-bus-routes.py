class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
#         ## 1. build a adj mapping for all stops 
#         adjMap  = defaultdict(list)
#         for route in routes:
#             for j in range(len(route)):
#                 start = route[j]
#                 others = route[:j] + route[j+1:]
#                 adjMap[start].extend(others)
        
#         # print(adjMap)
        
#         ## 2. bfs traverse 
#         q = deque()
#         q.append(source)
        
#         seen = set()
#         count = 0
#         found = False
        
#         while q:
#             count += 1
#             for _ in range(len(q)):
#                 src = q.pop()
#                 if src in seen:
#                     continue
#                 seen.add(src)
#                 for dst in adjMap[src]:
#                     if dst == target:
#                         return count
#                     q.append(dst)
#             # print(q)

#         return -1

        adjMap  = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                adjMap[stop].append(i)

        q = deque()
        q.append(source)

        seen = set()
        count = 0

        while q:
            count += 1
            for _ in range(len(q)):
                src = q.popleft()
                if src == target:
                    return count - 1
                for bus in adjMap[src]:
                    if bus in seen:
                        continue
                    seen.add(bus)
                    for stop in routes[bus]:
                        q.append(stop)

        return -1