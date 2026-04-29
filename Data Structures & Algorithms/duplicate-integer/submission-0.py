class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for num in nums:
            sett.add(num)
        return not len(sett) == len(nums)