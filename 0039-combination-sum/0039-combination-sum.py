class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            # base case: valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # invalid case
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # choose
                path.append(num)

                # reuse same number allowed → i (not i+1)
                backtrack(i, path, remaining - num)

                # undo
                path.pop()

        backtrack(0, [], target)
        return result