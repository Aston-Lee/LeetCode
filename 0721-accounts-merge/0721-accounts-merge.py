class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        mailAppear = defaultdict(list)
        
        totalappear = set()
        for i in range(len(accounts)):
            for mail in accounts[i][1:]:
                mailAppear[mail].append(i)

        visited = [False]*len(accounts)
        def dfs(index, emailSet):
            if visited[index]:
                return 
            visited[index] = True
            
            for mail in accounts[index][1:]:
                emailSet.add(mail)
                
                for neighborIndex in mailAppear[mail]:
                    dfs(neighborIndex, emailSet)
            return 
        
            
            
        res = []
        for i, (name, *account) in enumerate(accounts):
            if visited[i]:
                continue
            mailSet = set()
            dfs(i, mailSet)
            res.append([name] + sorted(list(mailSet)))
        
        return res 
            
        
            
            
        
#         [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        
        total [0,1,2,3]
        merged [0,1]
        "johnsmith@mail.com" [0,1]
        "john_newyork@mail.com" [0,2]
        "john00@mail.com" [1]
        "mary@mail.com" [2]
        "johnnybravo@mail.com" [3]

            
            