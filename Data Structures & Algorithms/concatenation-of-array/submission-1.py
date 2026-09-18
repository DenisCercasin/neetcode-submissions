class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_array = nums
        nums_length = len(nums_array)
        ans = []
        i = 0
        while i < nums_length:
            ans.append(nums_array[i])
            i+=1
        i = 0
        while i<nums_length:
            ans.append(nums_array[i])
            i+=1
        return ans