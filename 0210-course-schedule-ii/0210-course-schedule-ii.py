class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degree = defaultdict(int)
        preMap = defaultdict(list)
        
        for crs, pre in prerequisites:
            in_degree[pre] += 1
            preMap[crs].append(pre)
            
        start_nodes = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                start_nodes.append(i)
        
        sorted_order = []
        while start_nodes:
            crs = start_nodes.popleft()
            sorted_order.append(crs)
            for pre in preMap[crs]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    start_nodes.append(pre)
        
        if len(sorted_order) == numCourses:
            return sorted_order[::-1]
        else:
            return []
                