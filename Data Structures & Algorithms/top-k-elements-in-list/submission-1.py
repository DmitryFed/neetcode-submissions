class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        resultset =[]
        cnt = 0
        for n in nums:
            cnt = nums.count(n)
            if cnt not in diction.keys():
                diction.setdefault(cnt,[n])
                continue
            if n not in diction[cnt]:
                diction[cnt].append(n)
                
        diction = dict(sorted(diction.items(),reverse=True))
        lst =  list(sum(diction.values(),[]))

        return  lst[:k]