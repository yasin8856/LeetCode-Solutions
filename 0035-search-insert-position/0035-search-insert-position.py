class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index = 0
        while len(nums) > 1:
            mid_index = len(nums) // 2
            
            if nums[mid_index] > target:
                nums = nums[:mid_index]
            elif nums[mid_index] < target:
                start_index += mid_index + 1
                nums = nums[mid_index + 1:]
            else:
                return start_index + mid_index
        
        # Eğer döngü biterse ve target elemanını bulamazsak, hedef elemanın nereye yerleştirileceğini belirleriz
        if len(nums) == 1 and nums[0] < target:
            return start_index + 1
        return start_index