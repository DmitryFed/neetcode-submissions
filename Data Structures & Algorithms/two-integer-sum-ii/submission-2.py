class Solution:
   
  def twoSum(self,numbers: list[int], target: int) -> list[int]:
    
    lptr = 0
    rptr = len(numbers)-1
    

    while(lptr < rptr):
        
        if numbers[rptr] + numbers[lptr] == target:
           return [lptr+1, rptr+1]
        
        elif numbers[lptr] + numbers[rptr] < target:
             lptr+=1
        else:
            rptr-=1