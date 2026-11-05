class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {}
        for ch in t:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1

        required_count = len(t)
        n = len(s)

        left = 0
        start_index = 0
        min_window_size = float("inf")

        for right in range(n):
            right_char = s[right]

            if right_char in mp:
                if mp[right_char] > 0:
                    required_count -= 1
                mp[right_char] -= 1
            else:
                mp[right_char] = -1

            while required_count == 0:
                current_window_size = right - left + 1

                if current_window_size < min_window_size:
                    min_window_size = current_window_size
                    start_index = left

                left_char = s[left]

                mp[left_char] += 1

                if left_char in t and mp[left_char] > 0:
                    required_count += 1

                left += 1

        if min_window_size == float("inf"):
            return ""

        return s[start_index : start_index + min_window_size]
