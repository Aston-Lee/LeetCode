class Solution:
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))
        print(adj)

        visit = [False] * (n + 1)
        answer = float(inf)
        answer = self.dfs(1, adj, visit, answer)
        return answer
        
        
    def dfs(self, node: int, adj: List[List[Tuple[int, int]]], visit: List[bool], answer: int) -> None:
        
        visit[node] = True
        for edge in adj[node]:
            answer = min(answer, edge[1])
            if not visit[edge[0]]:
                answer = self.dfs(edge[0], adj, visit, answer)

        return answer
    

        