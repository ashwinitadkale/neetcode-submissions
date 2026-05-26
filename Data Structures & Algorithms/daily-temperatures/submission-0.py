class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prevIndex=stack.pop()
                ans[prevIndex]=i-prevIndex
            stack.append(i)
        return ans