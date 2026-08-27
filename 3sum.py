class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplet = [nums[i], nums[j], nums[k]]
                            triplet.sort()
                            if triplet not in result:
                                result.append(triplet)

        return result
