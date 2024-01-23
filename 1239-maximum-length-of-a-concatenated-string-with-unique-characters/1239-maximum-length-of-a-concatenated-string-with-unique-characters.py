class Solution:
    def maxLength(self, arr: List[str]) -> int:        
        # Use depth first search recursion through arr
        # building from an initial empty string
        return self.dfs(arr, 0, "")
    
    
    def dfs(self, arr: List[str], pos: int, res: str) -> int:        
        # Use a set to check res for duplicate characters
        if len(res) != len(set(res)):
            return 0

        # Recurse through each possible next option
        # and find the best answer
        best = len(res)
        for i in range(pos, len(arr)):
            best = max(best, self.dfs(arr, i + 1, res + arr[i]))
        return best