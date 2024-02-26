class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = defaultdict(list)
        indegree = defaultdict(int)
        startNode = set([i for i in range(numCourses)])
        
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            indegree[crs] += 1
            if crs in startNode:
                startNode.remove(crs)
            
            
        dq = deque(list(startNode))
        
        res = []
        while dq:
            for _ in range(len(dq)):
                i = dq.popleft()
                res.append(i)
                for crs in preMap[i]:
                    indegree[crs] -= 1
                    if indegree[crs] == 0:
                        dq.append(crs)
                        
        return res if len(res) == numCourses else []
                        
        
            
            