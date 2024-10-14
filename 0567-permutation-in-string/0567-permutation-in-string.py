from collections import Counter

class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = Counter(s1)
        window_counter = Counter(s2[:len(s1)])
        if window_counter == count_s1:
            return True
        for i in range(len(s1),len(s2)):
            window_counter[s2[i]] += 1
            window_counter[s2[i - len(s1)]] -=1
            if count_s1 == window_counter:
                return True
        return False

