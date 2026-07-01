class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        slow = 0
        fast = 1
        res = []
        while slow<len(temperatures)-1:
            if fast==len(temperatures):
                res.append(0)
                slow+=1
                fast=slow+1
            elif temperatures[slow]<temperatures[fast]:
                res.append(fast-slow)
                slow+=1
                fast=slow+1
            else:
                fast+=1
        res.append(0)
        return res
