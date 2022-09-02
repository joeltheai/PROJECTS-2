from typing import List



class Solution:

    def topKFrequent(self, nums: List[int], element: int) -> List[int]:
        memo = {}
        l = []


        for i in nums:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] = memo[i] + 1
 




       
        while element>0:
            maximum = 0
            p = 0
            for i in memo:
                if memo[i] > maximum:
                    maximum = i
                    p = i
            l.append(maximum)
            del memo[p]
            element = element-1
        return l

print(Solution.topKFrequent(1,[1,1,1,2,2,3],2))

print("hello world")
print("i love ubuntu")



