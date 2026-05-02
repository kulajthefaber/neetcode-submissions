import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        sorted_dict_desc = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))

        for i in range(k):
            ithkey = list(sorted_dict_desc)[i]
            output.append(ithkey)

        return output