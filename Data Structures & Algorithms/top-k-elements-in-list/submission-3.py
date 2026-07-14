class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        for n in nums:
            if n not in diction:
                diction[n] = 1
            else:
                diction[n]+=1
        
        resultset = sorted(diction,key=lambda x:diction[x],reverse=True)
        
        return resultset[:k]