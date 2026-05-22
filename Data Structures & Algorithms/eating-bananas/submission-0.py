import math

class Solution:
    def minEatingSpeed(self, piles, h):

        def canEat(k):

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / k)

            return total_hours <= h


        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left