class TrieNode:
    def __init__(self):
        self.child = {} # {char: Node}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def dfs(self, node, word):
        for i, char in enumerate(word):
            if char == ".":
                if node.child == {}:
                    return False #waht 
                for childnode in node.child.values():
                    if self.dfs(childnode, word[i+1:]):
                        return True
                return False
            elif char not in node.child.keys():
                return False
            node = node.child[char]
        return node.isEnd 
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.child.keys():
                node.child[char] = TrieNode()
            node = node.child[char]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for i, char in enumerate(word):
            if char == ".":
                for childnode in node.child.values():
                    if self.dfs(childnode, word[i+1:]):
                        return True
                return False
            elif char not in node.child.keys():
                return False
            node = node.child[char]
        return node.isEnd
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)