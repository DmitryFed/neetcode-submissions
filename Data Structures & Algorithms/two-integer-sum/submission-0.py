class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        step = 1
        match = {}
        for i in range(len(nums)):
            if (target - nums[i]) in match:
                return [match[target - nums[i]], i]
            else:
                match[nums[i]] = i