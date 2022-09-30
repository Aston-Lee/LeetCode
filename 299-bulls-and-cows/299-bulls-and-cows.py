class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
#         ## concept
#         1 8 0 7
#         7 8 1 0
        
#         sdict = {1: 1->0 , 0: 1->0}
#         gdict = {7: 1->0}  
        
#         1123
#         0111
        
#         sdict = {1:1->0,2:1 }
#         gdict = {0:1, }
        
        A, B = 0, 0
        sdict = {}
        gdict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] in gdict.keys() :
                    if gdict[secret[i]] > 0:
                        gdict[secret[i]] -= 1
                        B += 1
                    elif gdict[secret[i]] == 0:
                        if secret[i] not in sdict.keys():
                            sdict[secret[i]] = 1
                        else:
                            sdict[secret[i]] += 1
                        
                elif secret[i] not in gdict.keys() :
                    if secret[i] not in sdict.keys():
                        sdict[secret[i]] = 1
                    else:
                        sdict[secret[i]] += 1
                    
                if guess[i] in sdict.keys() and sdict[guess[i]] > 0:
                    sdict[guess[i]] -= 1
                    B += 1

                elif (guess[i] not in sdict.keys() or sdict[guess[i]] == 0):
                    if guess[i] not in gdict.keys():
                        gdict[guess[i]] = 1
                    else:
                        gdict[guess[i]] += 1
                
                print("secret[i]", int(secret[i]), "sdict: ",sdict)
                print("guess[i] ", int(guess[i]), "gdict: ",gdict)
                print("--------")

            
        return str(A)+'A'+str(B)+'B'
                    