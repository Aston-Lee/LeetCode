class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        deduct = sum(prices[:2])
        return money-deduct if deduct <= money else money