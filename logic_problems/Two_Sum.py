class Solution(object ):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i, j]
nums = [2, 11, 7, 15]
target = 4
sol = Solution()
print(sol.twoSum(nums, target))
