class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
# [1,2,3,6,2,3,4,7,8]
# 3

# 8

# tmp 6 7 
# index 0
        
        
        if len(hand) % groupSize:
            return False
        
        hand = sorted(hand)
        index = 0
        tmp = []
        while hand:
            if len(tmp) == groupSize:
                tmp = []
                index= 0 
            else:
                if tmp == [] or hand[index] == tmp[-1] + 1:
                    tmp.append(hand[index])   
                    hand.pop(index)
                elif hand[index] == tmp[-1]:
                    index += 1
                elif hand[index] > tmp[-1] + 1:
                    return False
                else:
                    print("unexpected")
                    
                if hand and index >= len(hand):
                    return False
                    
        return True
        
        
        