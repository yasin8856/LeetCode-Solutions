class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Eğer k, 1 ise tüm elemanlar aynı olduğu için fark sıfırdır
        if k == 1:
            return 0
        
        # Listeyi sıralıyoruz
        nums.sort()

        # Başlangıçta minimum farkı büyük bir değerle başlatıyoruz
        min_diff = float('inf')

        # k boyutlu alt gruplar oluşturuyoruz ve en büyük-en küçük farkını buluyoruz
        for i in range(len(nums) - k + 1):
            curr_diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, curr_diff)
        
        return min_diff
