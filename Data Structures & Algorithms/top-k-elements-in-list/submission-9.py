class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        sorted_dict_desc = (sorted(map.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            ithkey = sorted_dict_desc[i][0]
            output.append(ithkey)

        return output