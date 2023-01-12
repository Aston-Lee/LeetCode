class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] 
        cur.isEnd = True 

    def search(self, word: str) -> bool:
        
        ## try using dfs to go down and search, dfs make sense
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for childnode in cur.children.values():
                        if dfs(i+1, childnode) == True:
                            return True
                    return False                        
                else:
                    if c in cur.children:
                        cur = cur.children[c]
                    else: 
                        return False
            return cur.isEnd
                    
                    
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)