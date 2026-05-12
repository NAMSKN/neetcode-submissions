class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            com = target  - num;
            if com in s:
                return [s[com], i]
            else:
                s[num] = i
        return []

