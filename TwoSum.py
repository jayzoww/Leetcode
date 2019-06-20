#TwoSum https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, pos in enumerate(nums): 
            temp = target - pos
            for index2, x in enumerate(nums[index1 + 1:], start = index1 + 1):
                if temp - x == 0:
                    return [index1, index2];
