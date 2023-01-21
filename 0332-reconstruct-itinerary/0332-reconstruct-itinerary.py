class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = { src : [] for src, dst in tickets }
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        output = ["JFK"]
        
        def dfs(src):
            if len(output) == len(tickets)+1:
                return True
            if src not in adj: ##why
                return False
            tmpadj = list(adj[src])
            for index, dst in enumerate(tmpadj):
                adj[src].pop(index)
                output.append(dst)
                if dfs(dst): 
                    return True
                output.pop()
                adj[src].insert(index,dst)
            return False
                
        dfs("JFK")
        
        return output       