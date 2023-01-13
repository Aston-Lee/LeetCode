class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        sorted_freq = sorted(freq.items(),  key=lambda x: x[1])
        
        res = []        
        for num, f in sorted_freq[::-1]:
            if len(res) == k:
                return res
            res.append(num)
        return res