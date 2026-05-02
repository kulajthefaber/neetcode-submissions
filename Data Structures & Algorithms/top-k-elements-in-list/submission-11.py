class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        arr = [[] for _ in range(len(nums)+1)]
        for key,v in map.items():
            arr[v].append(key)

        count = 0
        for arr_i in reversed(arr):
            if count >= k:
                break

            if arr_i and count < k:
                for v in arr_i:
                    if count >=k:
                        break

                    if count < k:
                        output.append(v)
                        count += 1

        return output