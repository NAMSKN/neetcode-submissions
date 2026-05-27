class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        flag = 0
        for i in nums:
            if i == 0: 
                flag += 1 
                i = 1
            mul = mul * i
            
        ans = []
        for i in nums:
            prod = 1
            if flag == 1: prod = 0 
            elif flag > 1: mul = 0
            else: prod = mul
            if i == 0: 
                i = 1
                prod = mul
            if prod == 0: val = 0 
            else: val = prod/i
            ans.append(int(val))
        
        return ans