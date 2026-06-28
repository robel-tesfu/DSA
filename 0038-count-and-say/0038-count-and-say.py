class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            result = self.rle(result)

        return result

    def rle(self, s: str) -> str:
        i = 0
        new_s = ""

        while i < len(s):
            count = 1

            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1

            new_s += str(count) + s[i]
            i += 1

        return new_s