class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ## union-find is not the case for this
        ## use adjency list by dfs with crs, prereq is much easier
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # print(preMap)
            
        def dfs(crsNum, seen) -> bool:
            if preMap[crsNum] == []:
                return True
            if crsNum in seen:
                return False
            for preNum in preMap[crsNum]:
                original_seen = seen
                if preNum in seen:
                    return False
                else:
                    seen.add(crsNum)
                    if not dfs(preNum, seen):
                        return False
                    seen.remove(crsNum)
                    preMap[crsNum] = []
            return True
        
        for i in range(numCourses):
            seen = set()
            if not dfs(i, seen):
                return False
        return True


