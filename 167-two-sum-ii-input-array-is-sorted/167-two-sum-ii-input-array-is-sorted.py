class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i, n in enumerate(numbers):
            if n in record.keys():
                return[record[n], i+1]
            else:
                record[target - n] = i+1
        