class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        split into 2 groups
        adj:{
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        color: {
            1: blue 
            2: red
            3: red
        }
        visited: 1, 2, 3
        dq = [3]
        current:  -> check 1 ,3
            check 1, color[2] != color[1]   okay
            check 3, color[2] != color[3]   not okay  -> return False
            if other not in color:
                if color[current] == 'red':
                    color[other] = 'blue'
                if color[current] == 'blue':
                    color[other] = 'red'
            else:
                if color[current] == color[other]:
                    return False 
        '''
        adj = defaultdict(list)
        self.visited = set()
        dq = deque()
        self.color = {} ## pot. bug
        
        for n1, n2 in dislikes:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def check(n):
            self.visited.add(n)
            dq.append(n)
            self.color[n] = 'blue'
            while dq:
                current = dq.popleft()
                for other in adj[current]:
                    # print(other)
                    if other not in self.visited:
                        dq.append(other)
                        self.visited.add(other)
                    if other not in self.color:
                        if self.color[current] == 'red':
                            self.color[other] = 'blue'
                        if self.color[current] == 'blue':
                            self.color[other] = 'red'
                    else:
                        # print(self.color[current], self.color[other])
                        if self.color[current] == self.color[other]:
                            return False 
            return True
                        
        for i in range(n):
            # print(i, self.visited)
            if i+1 not in self.visited:
                if not check(i+1):
                    return False
                
        return True
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def bfs(source):
#             q = deque([source])
#             color[source] = 0 # Start with marking source as 'RED'
#             while q:
#                 print(q)
#                 node = q.popleft()
#                 print(node)
#                 for neighbor in adj[node]:
#                     # If there is a conflict, return false.
#                     if color[neighbor] == color[node]: return False
#                     if color[neighbor] == -1:
#                         color[neighbor] = 1 - color[node] # 1-1=0, 1-0=1
#                         q.append(neighbor)
            
#             return True
        
#         adj = [[] for _ in range(n + 1)]
#         for dislike in dislikes:
#             adj[dislike[0]].append(dislike[1])
#             adj[dislike[1]].append(dislike[0])
        
#         color = [-1] * (n + 1) # 0 stands for red and 1 stands for blue.
#         for i in range(1, n + 1):
#             if color[i] == -1:
#                 # For each pending component, run BFS.
#                 if not bfs(i):
#                     # Return false, if there is conflict in the component.
#                     return False
        
#         return True