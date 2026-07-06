class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        key =""
        
        for str in strs:
            key = "".join(sorted(str))
            words[key].append(str)

        return list(words.values())
