class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = "".join(char for char in s if char.isalnum()).lower()
        lptr = 0
        rptr = len(s1)-1
        
        while rptr >= lptr:
            
            if s1[rptr] != s1[lptr]: return False
        
            lptr +=1
            rptr -=1
            
        return True
            