class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        left = 0
        best_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in last_seen and last_seen[current_char] >= left:
                left = last_seen[current_char] + 1

            last_seen[current_char] = right

            best_length = max(best_length, right - left + 1)

        return best_length
