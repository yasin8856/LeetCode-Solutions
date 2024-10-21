class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_hash = {}
        not_once = []
        for i in nums:
            if i not in nums_hash:
                nums_hash[i] = 1  # İlk kez gördüğünüzde 1 olarak ayarlayın
            else:
                nums_hash[i] += 1  # Eğer tekrar görülmüşse sayısını artırın
                if i not in not_once:
                    not_once.append(i)  # Sadece sayının kendisini ekleyin
        return not_once
        