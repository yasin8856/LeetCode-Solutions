class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j =0,0
        
        # Ortadan başlamak için i ve j'yi tanımladık, ancak karşılaştırmaları iki diziye uygun şekilde yapmamız gerekiyor.
        while  i < len(nums1) and  j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]  # Ortak eleman bulundu
            elif nums1[i] < nums2[j]:
                # nums1'de ilerliyoruz, fakat aynı anda j'yi ilerletmemeliyiz
                i += 1
            else:
                # nums2'de ilerliyoruz, fakat aynı anda i'yi ilerletmemeliyiz
                j += 1
        
        return -1  # Ortak eleman bulunmadı
'''
i, j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
        return -1

starting_index = 0
        last_index = len(nums1) -1
        j = 0
        while starting_index <= last_index:
            mid_index = starting_index + (last_index - starting_index) // 2
            mid_value = nums1[mid_index]
            if nums2[j] == mid_value:
                return mid_value
            elif nums2[j] < mid_value:
                if mid_index == 0:
                    j+=1
                else:
                    last_index = mid_index -1
            elif nums2[j] > mid_value:
                starting_index = mid_index +1
            
        return -1

for i in nums1:
    for j in nums2:
        if i == j:
            return j
return -1
'''