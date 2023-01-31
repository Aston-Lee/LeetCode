class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        ## build the adj list
        emailMap = defaultdict(list)
        for i, (_, *account) in enumerate(accounts):
            for j in range(len(account)):
                email = account[j]
                emailMap[email].append(i)
                
        ## DFS function traverse account
        visitedAccounts = [False] * len(accounts)
        def dfs(i, emails):
            if visitedAccounts[i]:
                return
            visitedAccounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emailMap[email]:
                    dfs(neighbor, emails)
        
        ## Main
        res = []
        for i, (name, *account) in enumerate(accounts):
            if visitedAccounts[i]:
                continue
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
        
        
        
        