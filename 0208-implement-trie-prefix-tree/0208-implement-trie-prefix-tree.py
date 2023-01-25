class TrieNode:
    def __init__(self):
        self.children = {} ## initialize dict to store the child right below
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node
        node.is_end = True ## normaly this is False, only set to True when loop throu all char
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.is_end == False:
            return False
        else:
            return True
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)