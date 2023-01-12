class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add the word to the Trie
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] 
        cur.isEnd = True 

    def search(self, word: str) -> bool:
        """
        Search the Trie for a word, using a DFS.
        """
        def dfs(i: int, node: TrieNode) -> bool:
            """
            A helper function that uses DFS to search the Trie.
            """
            if i == len(word):
                return node.isEnd
            
            c = word[i]
            if c == '.':
                for child_node in node.children.values():
                    if dfs(i+1, child_node) == True:
                        return True
                return False
            else:
                if c in node.children:
                    return dfs(i+1, node.children[c])
                else:
                    return False
                
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)