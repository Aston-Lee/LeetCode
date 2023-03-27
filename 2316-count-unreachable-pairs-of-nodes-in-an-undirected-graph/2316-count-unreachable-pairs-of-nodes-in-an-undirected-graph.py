class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # create a new UnionFind object with n elements
        dsu = UnionFind(n)
        
        # merge connected components of the graph
        for edge in edges:
            dsu.union_set(edge[0], edge[1])
        
        # count the size of each component
        componentSize = {}
        for i in range(n):
            componentSize[dsu.find(i)] = componentSize.get(dsu.find(i), 0) + 1
        
        # calculate the number of pairs of nodes in different components
        numberOfPaths = 0
        remainingNodes = n
        for component in componentSize.values():
            numberOfPaths += component * (remainingNodes - component)
            remainingNodes -= component
        
        return numberOfPaths
