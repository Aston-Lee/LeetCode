class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pair = [(p,s) for p, s in zip(position, speed)]
        # print(pair)
        
        stack = []
        for p, s in sorted(pair):
            time = (target-p) / s
            # print(time)
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
            