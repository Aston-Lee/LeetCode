class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # arr = [gas[i]-cost[i] for i in range(len(gas))]
        # if sum(arr) < 0:
        #     return -1
        # else:
        #     total, remain = 0, 0
        #     start = 0
        #     for i in range(len(arr)):
        #         total += gas[i]-cost[i]
        #         remain += gas[i]-cost[i]
        #         if remain < 0:
        #             remain = 0
        #             start = i+1
        #     return start 
        
        total, remain = 0, 0
        start = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            remain += gas[i]-cost[i]
            if remain < 0:
                remain = 0
                start = i+1
        return start if total>=0 else -1
                
                
                # if arr[i] >= 0:
                #     balance = arr[i]
                #     dst = i
                #     pos = i+1
                #     if pos == len(gas):
                #         pos = 0
                #     while pos != dst:
                #         balance += arr[pos]
                #         if balance < 0:
                #             break
                #         pos += 1
                #         if pos == len(gas):
                #             pos = 0
                #     if pos == dst:
                #         return i