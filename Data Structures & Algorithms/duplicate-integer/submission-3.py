class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_array = nums
        nums_len = len(nums_array)
        response = False
        seen = set()

        for i in range(nums_len):
            if nums_array[i] in seen:
                response = True
                return response
            else:
                seen.add(nums_array[i])
        return response