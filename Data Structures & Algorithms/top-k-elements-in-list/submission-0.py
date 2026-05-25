from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = Counter(nums)
        # Sort items by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # Take top k keys
        return [item[0] for item in sorted_items[:k]]
