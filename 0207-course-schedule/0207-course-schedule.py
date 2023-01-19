class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1

        queue = [i for i in range(numCourses) if indegree[i] == 0]
        cnt = 0
        while queue:
            cnt += 1
            node = queue.pop(0)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return cnt == numCourses