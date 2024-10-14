from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        count = {}
        start = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            while count[s[end]] > 2:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len