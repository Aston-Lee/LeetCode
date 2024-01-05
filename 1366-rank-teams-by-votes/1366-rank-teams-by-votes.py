class Solution:
    def rankTeams(self, votes: List[str]) -> str:
    
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1
            print(d)

        voted_names = sorted(d.keys())
        print("voted_names:", voted_names)
        print(sorted(voted_names, key=lambda x: d[x], reverse=True))
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
        ## reverse = True
                
            
        
        
        