# class UnionFind:
#     def __init__(self, size):
#         self.parent = list(range(size))
#         self.rank = [0] * size

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union_set(self, x, y):
#         xset = self.find(x)
#         yset = self.find(y)
#         if xset == yset:
#             return
#         elif self.rank[xset] < self.rank[yset]:
#             self.parent[xset] = yset
#         elif self.rank[xset] > self.rank[yset]:
#             self.parent[yset] = xset
#         else:
#             self.parent[yset] = xset
#             self.rank[xset] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                rank[p1] += 1
        
        
        for edge in edges:
            union(edge[0], edge[1])
        
        componentSize = {}
        for i in range(n):
            componentSize[find(i)] = componentSize.get(find(i), 0) + 1
        
        numberOfPaths = 0
        remainingNodes = n
        for component in componentSize.values():
            numberOfPaths += component * (remainingNodes - component)
            remainingNodes -= component
        
        return numberOfPaths
