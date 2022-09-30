class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones)
        while(len(stones)>1):
            stones.append(stones.pop() - stones.pop())
            stones = sorted(stones)
        
        return stones[0]