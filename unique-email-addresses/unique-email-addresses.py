class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        emailset = set()
        
        for email in emails:
            mouse = None
            buffer = ""
            discard = False
            for i, char in enumerate(email):
                if char == '@':
                    mouse = i
                    break
                elif discard == True or char == '.':
                    continue
                elif char == '+':
                    discard = True 
                else:
                    buffer += char
            realemail = buffer + "@" + email[mouse+1:]
            emailset.add(realemail)
        return len(emailset)
        