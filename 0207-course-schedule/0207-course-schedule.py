class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        cycle = set() #record every loop, if there's a cycle
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True
            
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True