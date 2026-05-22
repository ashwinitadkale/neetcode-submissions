class Solution:
    def shipWithinDays(self, weights, days):

        def canShip(capacity):

            days_used = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > capacity:
                    days_used += 1
                    current_weight = 0

                current_weight += weight

            return days_used <= days


        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left
        