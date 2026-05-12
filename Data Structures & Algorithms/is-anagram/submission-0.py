class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if "".join(sorted(t)) == "".join(sorted(s)) else False
        