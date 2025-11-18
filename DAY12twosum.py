class Solution:
    def twoSum(self, nums:list[int], target:int )-> list[int]:
        hash_map = {}
        for n, i in enumerate(nums):
            diff= target -i
            if diff in hash_map:
                return [hash_map[diff], n]
            hash_map[i] = n
        return