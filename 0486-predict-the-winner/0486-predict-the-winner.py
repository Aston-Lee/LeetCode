class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''

        
        '''

        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True

        dp = [[0] * n for _ in range(n)]

        for leftIndex in range(n):
            dp[leftIndex][leftIndex] = nums[leftIndex]

        for length in range(2, n + 1):
            for leftIndex in range(n - length + 1):
                rightIndex = leftIndex + length - 1
                dp[leftIndex][rightIndex] = max(nums[leftIndex] - dp[leftIndex + 1][rightIndex], nums[rightIndex] - dp[leftIndex][rightIndex - 1])

        return dp[0][n - 1] >= 0
