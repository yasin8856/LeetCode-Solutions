class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort() #aradaki farkı en aza indirmek için sıralıyoruz
        min_diff = max(nums)

        for i in range(len(nums) - k +1):
            curr_diff = nums[i + k -1] - nums[i]
            min_diff = min(min_diff, curr_diff)
        return min_diff 