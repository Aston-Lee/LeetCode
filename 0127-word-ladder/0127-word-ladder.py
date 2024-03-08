class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        
        adj = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i]+'*'+word[i+1:]].add(word)
                
        for key, val in adj.items():
            adj[key] = list(val)
            
        
        dq = deque([beginWord])
        visited = set()
        degree = 0
        while dq:
            # print(dq)
            degree += 1
            for _ in range(len(dq)):
                word = dq.popleft()
                if word == endWord:
                    return degree
                if word in visited:
                    continue
                for i in range(len(word)):
                    adjWord = word[:i]+'*'+word[i+1:]
                    # print("adjWord: ", adjWord)
                    if adjWord in adj:
                        ls = adj[adjWord]
                        for lsword in ls:
                            if lsword not in visited:
                                dq.append(lsword)
                    
                visited.add(word)
                adj[word] = []
                
        return 0
                
        