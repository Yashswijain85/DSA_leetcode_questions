class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return ""
        anagram_dict = {}

        for word in strs:
            if "".join(sorted(word)) in anagram_dict:
                anagram_dict["".join(sorted(word))].append(word)
            else:
                anagram_dict["".join(sorted(word))] = [word]
        return [val for val in anagram_dict.values()]


# Time complexity -- O(k.log(k)) -- k(length of each string)
# Space complexity -- O(n.k) 
