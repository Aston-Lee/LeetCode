import numpy as np

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        #..*##
        
        
        m, n = len(box), len(box[0])
        
        for i in range(m):
            rightmost = n - 1  # Reset the rightmost for each row

            for j in range(n - 1, -1, -1):
                if box[i][j] == '#':
                    box[i][j], box[i][rightmost] = '.', '#'  # Swap stone with the rightmost empty space
                    rightmost -= 1  # Update the rightmost position
                elif box[i][j] == '*':
                    rightmost = j - 1  # Reset rightmost position when an obstacle is encountered
        
        newbox = np.transpose(box)
        for i in range(len(newbox)):
            newbox[i] = newbox[i][::-1]
        
        return newbox
                
        