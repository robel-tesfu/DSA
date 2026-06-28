class Solution:
    def searchRange(self, nums, target):
        def findFirst():
            left, right = 0, len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # go left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return res

        def findLast():
            left, right = 0, len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # go right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return res

        return [findFirst(), findLast()]