class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        '''
        dfs
        bfs 
        2 pointer
        
        recipes = ["bread","sandwich","burger"], 
        ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
        supplies = ["yeast","flour","meat"]
           
        recipesSet = set(["bread","sandwich","burger"]) 
        validSupplies = set(["yeast","flour","meat","bread","sandwich"])
        
        dfs(burger)
        ings = ["sandwich","meat","bread"]
        

        
        '''
        
        n = len(recipes)

        # DAG: ingredients --> recipes
        g = defaultdict(list)
        # default indegree is 0
        indegree = defaultdict(int)

        # Create Gragh and add indegree
        # for i in range(n):
        #     for ing in ingredients[i]:
        #         indegree[recipes[i]] += 1
        #         g[ing].append(recipes[i])
                
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                indegree[recipe] += 1
                g[ing].append(recipe)
            

        # initally queue has all supplies 
        # assuming only ingredients provided
        q = deque(supplies)

        while q:
            curr = q.popleft()
            for nei in g[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = []
        # for all recipes, it would have indegree of 0 
        # so that it can be cooked
        for rec in recipes:
            if indegree[rec] == 0:
                res.append(rec)

        return res

        
        
        
#         validSupplies = set(supplies)
#         # validIngredients = set(ingredients)
#         recipesSet = set(recipes)
#         rec2ing = {}
#         ans = []
        
#         def dfs(recipe): ## return True if recipe can be formed by supplies
#             ings = ingredients[rec2ing[recipe]]
#             valid = True 
#             for ing in ings:
#                 if ing not in validSupplies:
#                     if ing in recipesSet:
#                         if dfs(ing):
#                             validSupplies.add(ing)
#                         else:
#                             valid = False
#                             break
#                     else:
#                         valid = False
#                         break
#             if valid:
#                 validSupplies.add(recipe)
#             return valid
                
            
        
#         for i, recipe in enumerate(recipes):
#             rec2ing[recipe] = i 
            
#         for recipe in recipes:
#             if dfs(recipe):
#                 ans.append(recipe)
                
#         return ans
    
    
        
            