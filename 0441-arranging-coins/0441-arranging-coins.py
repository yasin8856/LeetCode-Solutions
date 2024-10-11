class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(1 + 8*n)-1)/2)







        """
        k = 1
        while (k * (k + 1)) // 2 <= n:
            k += 1
        return k - 1

        m = 0
        for i in range(1, n + 1):  # 1'den başlıyoruz çünkü ilk sıra 1 bozuk para
            m += i  # Kullanılan bozuk para sayısı
            if m == n:  # Tamamlanmış bir sıra
                return i
            elif m > n:  # Eğer kalan bozuk paralar tam bir sıra oluşturmuyorsa
                return i - 1
        
        return 0  # Eğer n = 0 olursa (bozuk para yok)
    """


'''
k = 1
while (k * (k + 1)) // 2 <= n:
    k += 1
return k - 1

counter, x = 0, 1
    while n>=x:
        n-=x
        counter+=1
        x+=1
    return counter
'''