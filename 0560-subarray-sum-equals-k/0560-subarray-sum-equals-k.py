class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        map = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in map:
                count += map[sum - k]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        return count
