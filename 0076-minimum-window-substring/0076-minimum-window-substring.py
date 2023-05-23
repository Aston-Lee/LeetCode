class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charSet = set(t)
        freq = Counter(t)
        counter = len(t)
        l, r = 0, 0
        start, length = 0, float('inf')

        while r < len(s):
            if freq[s[r]] > 0:
                counter -= 1
            freq[s[r]] -= 1
            r += 1

            while counter == 0:
                if r - l < length:
                    start, length = l, r - l

                freq[s[l]] += 1
                if freq[s[l]] > 0:
                    counter += 1
                l += 1

        if length == float('inf'):
            return ""
        return s[start:start+length]
