from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(1)

        pre = 1
        pos = 1

        # pre = nums[0]
        # pos = nums[len(nums)-1]

        for i in range(0, len(nums)-1):
            pre *= nums[i]
            l[i+1] = l[i+1] * pre
        # print(l)

        for i in range(len(nums)-1, 0, -1):
            pos *= nums[i]
            l[i-1] = l[i-1] * pos
        return l


print(Solution.productExceptSelf(1, [1, 4, 2, 0, 9]))
print(Solution.productExceptSelf(1, [5, 3, 2, 1]))
