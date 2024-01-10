# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ''' 
        representing value?
        child: {
            1: [5,3]
            5: [4]
            4: [9,2]
            3: [10, 6]
        }
        parent: {
            3: 1
            10:3
            6: 3
            5: 1
            4: 5
            9: 4
            2: 4
        }
        infected: set(3, 10, 6, 1, 5, 4)
        deque= []
        current 4
        time 
        '''
        child = defaultdict(list)
        parent = {}
        def dfs(node):
            
            if node.left:
                parent[node.left.val] = node.val
                child[node.val].append(node.left.val)
                dfs(node.left)
            
            if node.right:
                parent[node.right.val] = node.val
                child[node.val].append(node.right.val)
                dfs(node.right)
                
            return 
        
        dfs(root)
        
        dq = deque([start])
        infected = set()
        time = 0
        while dq:
            for _ in range(len(dq)):
                current = dq.popleft()
                infected.add(current)
                for c in child[current]:
                    if c not in infected:
                        dq.append(c)
                if current in parent and parent[current] not in infected:
                    dq.append(parent[current])
            
            time += 1
            
        return time-1
            