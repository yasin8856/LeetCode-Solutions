class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_hash = {}
        not_once = []
        for i in nums:
            if i not in nums_hash:
                nums_hash[i] = 1
            else:
                nums_hash[i] += 1
                if i not in not_once:
                    not_once.append(i)
        return not_once
        