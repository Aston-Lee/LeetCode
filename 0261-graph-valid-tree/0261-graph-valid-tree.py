class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # check 1. nodes quantity
        # check 2. cycles 
        # check 3. all connected
        
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
        if len(edges) < n-1:
            return False
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2: 
                r1, r2 = rank[p1], rank[p2]
                if r1 >= r2:
                    parent[p2] = parent[p1]
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = parent[p2]
                    rank[p2] += rank[p1]
                return True # because it will return 0, if didnt specify this will encounter failure
            else:
                return False
                
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        if max(rank) == n:
            return True
        else:
            return False
        