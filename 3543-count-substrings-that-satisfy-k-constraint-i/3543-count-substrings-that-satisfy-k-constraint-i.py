class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            zeros = 0
            ones = 0
            for j in range(i , n):
                if s[j] == '1':
                    ones +=1
                else:
                    zeros +=1    
                if ones > k and zeros > k:
                    break
                else:
                    count +=1
        return count