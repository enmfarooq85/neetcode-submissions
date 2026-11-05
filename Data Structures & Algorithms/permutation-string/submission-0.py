class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        need = [0] * 26
        window = [0] * 26

        aCode = ord("a")

        for ch in s1:
            need[ord(ch) - aCode] += 1

        left = 0

        for right in range(n2):
            window[ord(s2[right]) - aCode] += 1

            if right - left + 1 > len(s1):
                window[ord(s2[left]) - aCode] -= 1
                left += 1

            if right - left + 1 == n1 and need == window:
                return True

        return False
