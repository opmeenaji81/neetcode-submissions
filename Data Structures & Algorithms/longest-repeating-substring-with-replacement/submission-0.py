class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        max_count = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            if max_count < count[s[right]]:
                max_count = count[s[right]]
            
            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
            
            
