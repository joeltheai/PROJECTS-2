print("hello World")

j = "jel"

print(j)
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        l = []
        while k>0:
            maxi = 0
            p = 0
            for i in d:
                if d[i] > maxi:
                    maxi = i
                    p = i
            l.append(maxi)
            del d[p]
            k = k-1
        return l

print(Solution.topKFrequent(1,[1,1,1,2,2,3],2))