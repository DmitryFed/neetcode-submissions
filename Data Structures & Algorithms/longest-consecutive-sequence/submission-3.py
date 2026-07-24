class Solution:
    def longestConsecutive(self,  nums: list[int]) -> int:
        
        if not nums: return 0
        
        numset = set(nums)
        
        dict_cnt = {}
        # Removed start_seq = 0 and counter = 1 initialization here
        for n in numset:
            
            if (n-1 not in(numset)):
                start_seq = n 
                dict_cnt[start_seq] = 1
                
                current_num = n + 1
                while current_num in numset:
                    dict_cnt[start_seq] += 1
                    current_num += 1
            
        return max(dict_cnt.values()) if dict_cnt else 1