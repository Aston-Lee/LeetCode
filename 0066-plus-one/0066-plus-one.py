class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) == 1:
                return [1,0]
            digits[-1] = 0
            addon = 1
            pos = len(digits)-2
            while addon:
                if digits[pos] == 9:
                    digits[pos] = 0
                    addon = 1
                else:
                    digits[pos] += 1 
                    addon = 0
                print(digits)
                pos -= 1
                if pos == -1:
                    break
                
            if addon:
                return [1]+ digits
            else:
                return digits
            