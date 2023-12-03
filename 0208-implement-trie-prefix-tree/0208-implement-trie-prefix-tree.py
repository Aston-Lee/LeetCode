class TrieNode:
    def __init__(self, char):
        self.isEnd = False
        self.childs = {}
        # self.char = ""
        
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.childs:
                node.childs[char] = TrieNode(char)
            node = node.childs[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.childs:
                return False
            else:
                node = node.childs[char]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.childs:
                return False
            else:
                node = node.childs[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)