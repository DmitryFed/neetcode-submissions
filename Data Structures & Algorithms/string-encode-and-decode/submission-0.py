class Solution:

    def encode(self, strs: List[str]) -> str:
        result =""
    
        for s in strs:
            result += str(len(s)) + "#" + s 
        
        return result    

    def decode(self, s: str) -> List[str]:
        
        delimiter ="#"
    
        delimiter_pos = -1
        
        str_len = 0
        
        str_pointer = -1
        
        result_arr = []
        
        while(str_pointer+1 < len(s)):
            
            delimiter_pos = s.find(delimiter,str_pointer+1)
        
            str_len = int(s[str_pointer+1:delimiter_pos])
        
            result_arr.append(s[delimiter_pos+1:delimiter_pos+str_len+1])
            
            str_pointer = delimiter_pos + str_len
            
        return result_arr
