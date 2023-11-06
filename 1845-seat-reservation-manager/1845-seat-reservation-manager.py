class SeatManager:

    def __init__(self, n: int):
        self.minheap = [i+1 for i in range(n)]
        heapq.heapify(self.minheap)
        

    def reserve(self) -> int:
        res = heapq.heappop(self.minheap)
        return res
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minheap, seatNumber)
        return None
        
        
# seats = [1, 2, 3, 4, 5]
# self.available = (1, 2, 3, 4, 5)
# self.minheap = [1, 2, 3, 4, 5]


# seats = [  3, 4, 5]
# self.available = ( 1, 3, 4, 5)
# self.minheap = [ 1, 3, 4, 5]

# unreserve 1 


        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)