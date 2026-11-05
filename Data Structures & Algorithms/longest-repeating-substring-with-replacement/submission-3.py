class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        mp = {}
        ans = 0

        left = 0
        for right in range(n):
            mp[s[right]] = 1 + mp.get(s[right], 0)

            # if window is invalid:
            # shrink the window
            while (right - left + 1) - max(mp.values()) > k:
                mp[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
