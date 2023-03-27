class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        def count(node):
            if node in visited:
                return 0
            visited.add(node)
            return sum(count(nei) for nei in adjList[node]) +1
        
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        
        total_edges = 0
        for vertex in range(n):
            if vertex not in visited:
                num_visited = count(vertex)
                num_unvisited = n - num_visited
                total_edges += num_visited * num_unvisited
        return total_edges//2