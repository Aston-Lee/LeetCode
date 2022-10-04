class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2 pointer solution
        output = ""
        for c in s:
            if c.isalnum():
            # if (ord('a')<=ord(c) and ord(c)<=ord('z')) or (ord('A')<=ord(c) and ord(c)<=ord('Z')) :
                output += c.lower()
        print(output)
        
        # 0 1 2 3 4 5  len 6 
        n = len(output)
        if len(output) == 2:
            return output[0] == output[1]
        
        for i in range(n/2, n):
            j = n-i-1
            print(output[i], output[j])
            if output[i]!=output[j]:
                return False
        # else: ## 0 1 2 3 4   len 5 
        #     for i in range(n+1/2,n):
        #         j = n-i-1
        #         if output[i]!=output[j]:
        #             return False
        
        
        # "0P" 0 1 len2
            
        
        return True
            
        