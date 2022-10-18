class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        count = Counter(nums)
        taken = []
        # taken = deque() ## usign deque is the same
        
        moves = 0
        for x in range(len(nums) + max_val):
            if count[x] > 1:
                taken.extend([x]*(count[x]-1))
            elif taken and count[x] == 0:
                n = taken.pop()
                # n = taken.popleft()
                print(n)
                moves += x-n
        
        return moves
        