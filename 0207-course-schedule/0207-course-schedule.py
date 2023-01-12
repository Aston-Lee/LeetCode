class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the prerequisites map 
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crsNum, seen) -> bool:
            # If there are no more prerequisites, return True
            if preMap[crsNum] == []:
                return True
            # If the course has already been seen, there is a cycle so return False
            if crsNum in seen:
                return False
            seen.add(crsNum)
            # Check the prerequisites of the current course
            for preNum in preMap[crsNum]:
                if not dfs(preNum, seen):
                    return False
            # Once all the prerequisites have been visited, remove the course from the seen set
            seen.remove(crsNum)
            # Mark the current course as finished traversing
            preMap[crsNum] = []
            return True
        
        # Check each course
        for i in range(numCourses):
            seen = set()
            if not dfs(i, seen):
                return False
        return True
