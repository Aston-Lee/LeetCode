class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        """
        [4, x] 矩陣
        P = [0,0]
        A = [1,0]
        Y = [2,0]
        P = [3,0] -> key 轉
        只有下跟右上 用key決定
        
        A = [2,1]
        L = [1,2]
        I = [0,3] -> key 轉 key 用正負號
        
        輸出:
        反過來讀
        [0,0]->[0,3]->[0,6] 增加 4-1
        [1,0]->[1,2]->[1,3]->  增加有規律 可不可以就直接輸出有的數值就好 
        作一個計數器知道矩陣範圍 if 只要不是null就輸出
        
        範圍計算
        
        """
        if numRows == 1:
            return s
        
        ceiling= math.ceil(math.ceil((len(s) - numRows)/(numRows-1))/2)
        cols = int(1 + (numRows-1)*ceiling) + numRows
        print(cols)
        
        matrix = [[0 for _ in range(cols)] for _ in range(numRows)]

        def down(local_i, local_j, string_counter):
        # local_i, string_counter = 0, 0
            while(local_i!=numRows and string_counter != len(s)):
                # print(local_i, local_j)
                matrix[local_i][local_j] = s[string_counter]
                local_i += 1
                string_counter += 1
            local_i -= 1
            if string_counter != len(s):
                right_up(local_i, local_j, string_counter)
            
        ## 右上
        def right_up(local_i, local_j, string_counter):
            while(local_i!=0 and string_counter != len(s)):
                local_i -= 1
                local_j += 1
                # print(local_i, local_j)
                matrix[local_i][local_j] = s[string_counter]
                string_counter += 1
            if string_counter != len(s):
                down(local_i+1, local_j, string_counter)
        
        down(0,0,0)
        
        ans = ""
        for i in range(numRows):
            for item in matrix[i]:
                if item !=0:
                    ans+=item
        return ans
            # if[matrix[i][0]!=0]:
            #     print(matrix[i][0])
            
        
        
        