class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # map = defaultdict(int)
        map = {}
        for i in range(n):
            diff = target - nums[i]
            for j in range(1,n):
                map[nums[j]] = j
                if diff in map and map[diff] != i:
                    return [i, map[diff]]
                # map[nums[i]] = i
        return []
