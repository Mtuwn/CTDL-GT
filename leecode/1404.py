class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        while s[-1] == '0':
            s = s[:-1]
            ans += 1

        if s == "1":
            return ans
        ans += 1
        for c in s:
            ans += 1 if c == '1' else 2

        return ans