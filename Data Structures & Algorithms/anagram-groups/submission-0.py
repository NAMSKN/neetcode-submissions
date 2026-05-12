class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in strs:
            str1 = "".join(sorted(i))
            if str1 not in hash:
                hash[str1] = []
            hash[str1].append(i)
        return list(hash.values())