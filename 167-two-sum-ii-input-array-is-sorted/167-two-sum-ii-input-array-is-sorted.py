class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # # normal approach
        # record = {}
        # for i, n in enumerate(numbers):
        #     if n in record.keys():
        #         return[record[n], i+1]
        #     else:
        #         record[target - n] = i+1
        
        # 2 pointer apporach
        lo = 0
        hi = len(numbers)-1
        
        while(lo!=hi):
            num = numbers[lo] + numbers[hi]
            if num == target:
                return [lo+1, hi+1]
            elif num > target:
                hi -= 1
            else:
                lo += 1
        
        