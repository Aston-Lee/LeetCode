class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currnum = 0
        tmpstr = ""
        for c in s: 
            if c.isdigit():
                currnum = currnum*10 + int(c)
            elif c == '[':
                stack.append(currnum)
                stack.append(c)
                currnum = 0
            elif c == ']':
                while(stack[-1]!='['):
                    n = stack.pop(-1)[::-1] ## note this 
                    tmpstr += n
                stack.pop(-1) #pop off the '['
                stack.append(tmpstr[::-1]*stack.pop(-1))
                tmpstr = ""
            else: # c is alphabet
                stack.append(c)
            # print(stack)
            
        tmpstr = ""
        for frag in stack:
            tmpstr += frag

        return tmpstr
       
            
    # def decodeString(self, s):
    #     stack = []; curNum = 0; curString = ''
    #     for c in s:
    #         if c == '[':
    #             stack.append(curString)
    #             stack.append(curNum)
    #             curString = ''
    #             curNum = 0
    #         elif c == ']':
    #             num = stack.pop()
    #             prevString = stack.pop()
    #             curString = prevString + num*curString
    #         elif c.isdigit():
    #             curNum = curNum*10 + int(c)
    #         else:
    #             curString += c
    #     return curString

        