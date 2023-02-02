class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        


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