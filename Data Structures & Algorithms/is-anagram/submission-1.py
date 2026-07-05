class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            letters[l] = letters.get(l,0) +1

        for  letter in t:
            if letter in letters.keys():
                letters[letter] -= 1
            else: return False  

        return not any(v != 0 for v in letters.values())