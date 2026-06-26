from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        prefix = [0]

        balance = 0
        for x in nums:
            if x == target:
                balance += 1
            else:
                balance -= 1
            prefix.append(balance)

        values = sorted(set(prefix))

        bit = Fenwick(len(values))
        ans = 0

        for p in prefix:
            idx = bisect_left(values, p)

            ans += bit.query(idx)

            bit.update(idx + 1, 1)

        return ans