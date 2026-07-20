class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefarr = []
        suffarr = []
        result =  []
        i = 0
        multiplier = 1
        cnt = len(nums)
        while(i < cnt ):
            
            multiplier *= nums[i] 
        
            prefarr.append(multiplier)      
            
            i+=1
        
        multiplier = 1 
        i = cnt -1  
        
        while(i >= 0):
            
            multiplier *= nums[i]
            
            suffarr.append(multiplier)
            
            i-=1
            
        i = 0
        
        for n in nums:
            if i == 0:
                result.append(suffarr[cnt-2])
            elif i == (cnt - 1):
                result.append(prefarr[cnt-2])
            else:
                result.append(prefarr[i-1] * suffarr[cnt-1-i-1])  
                
            i+=1
                        
        return result

        