class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         checked_numbers = {}
         for i in nums:
            if i in checked_numbers.keys():
                return True
            else: checked_numbers[i] = 1
         return False
