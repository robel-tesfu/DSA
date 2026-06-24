class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            # if pattern finished
            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # check if next is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # 2 choices:
                # 1) skip x*
                # 2) use it if first matches
                return (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )

            # normal match
            return first_match and dp(i + 1, j + 1)

        return dp(0, 0)