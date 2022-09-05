from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], element: int) -> List[int]:
        l = []
        for i in nums:
            l.append(1)
        
        pre = 1
        pos = 1
         
        return l


print(Solution.topKFrequent(1, [1, 1, 1, 2, 2, 3], 2))


