import collections
# from heapq import heappop, heappush, heappushpop, heapify
from sortedcontainers import SortedSet



class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))
            
        print(self.food_rating_map, self.food_cuisine_map, self.cuisine_food_map)
        

    def changeRating(self, food: str, newRating: int) -> None:
        
        cuisine = self.food_cuisine_map[food]
        ## find the old element and remove it
        old_element = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine].remove(old_element)
        
        ## add the new element 
        self.cuisine_food_map[cuisine].add((-newRating, food))
        self.food_rating_map[food] = newRating
    
    
    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_map[cuisine][0][1]
        
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)



# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

# ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
# ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
# [9, 12, 8, 15, 14, 7]

# korean: (9, kimchi), (7, bulgogi) -> (O(N) search and change)
# japanese : (14, ramen) (12, miso), (8, sushi), 
# greek: (15, moussaka)
    
# largest:{
#     korean: (9, kimchi)
#     japanese : (14, ramen)
#     greek: (15, moussaka)
# }
    