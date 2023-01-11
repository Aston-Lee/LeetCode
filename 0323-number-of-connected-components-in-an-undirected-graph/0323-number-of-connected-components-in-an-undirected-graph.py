class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        ## union find 
        ## every union:  res -= 1 
        
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        self.res = n
        
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
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                self.res -= 1
        
        for n1, n2 in edges:
            union(n1, n2)
            
        return self.res
                