class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            valor_meio = nums[mid]

            if valor_meio == target:
                return mid
            elif valor_meio < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


nums = [-1, 0, 2, 4, 6, 8]
target = 4
sol = Solution()
print(sol.search(nums, target)) 