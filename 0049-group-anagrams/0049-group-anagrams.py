from collections import Counter
class Solution:
    #Motham youtube
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in group:
                group[sorted_word]=[]
            group[sorted_word].append(word)
        return list(group.values())
        