class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left += 1
            longest = max(longest, len(s[left:right+1]))
        return longest
            

