class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        return res
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = ""
        ans = []
        num = 0
        i = 0
        while i != len(s):
            if s[i].isdigit():
                num *= 10
                num += int(s[i])
                i += 1
            elif s[i] == '#':
                i += 1
                ans.append(s[i:i+num])
                i += num
                num = 0

        return ans 
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))