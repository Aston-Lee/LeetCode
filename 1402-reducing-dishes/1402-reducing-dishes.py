class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        max_satisfaction = 0
        suffix_sum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            if suffix_sum + satisfaction[i] > 0:
                suffix_sum += satisfaction[i]
                max_satisfaction += suffix_sum
            else:
                break

        return max_satisfaction
