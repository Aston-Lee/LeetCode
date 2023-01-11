class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1 for _ in range(n+1)]
        
        def find(n): #find the root
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            else:
                r1, r2 = rank[p1], rank[p2]
                if r1 >= r2:
                    parent[p2] = p1
                    rank[p1] += p2
                else:
                    parent[p1] = p2
                    rank[p2] += p1
                return False
                
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
            