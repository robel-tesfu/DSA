class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # 🔥 skip duplicates at same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]

                path.append(num)

                # move forward ONLY (no reuse)
                backtrack(i + 1, path, remaining - num)

                path.pop()

        backtrack(0, [], target)
        return result