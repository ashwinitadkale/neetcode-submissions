class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        # count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # sort by frequency
        arr = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(arr[i][0])

        return res