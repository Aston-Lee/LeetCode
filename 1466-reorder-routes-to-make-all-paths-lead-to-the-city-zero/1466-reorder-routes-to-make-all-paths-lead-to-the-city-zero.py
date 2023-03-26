class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(set)
        for u, v in connections:
            adjList[u].add((v, True))
            adjList[v].add((u, False))
        
        # print(adjList)
        
        queue = deque([0])
        visited = set([0])
        
        changeEdges = 0
        while queue:
            node = queue.popleft()
            
            for neighbor, isConnection in adjList[node]:
                if neighbor not in visited:
                    changeEdges += isConnection
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return changeEdges