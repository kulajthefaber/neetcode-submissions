from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_list = []
        map = {}

        for i, strr in enumerate(strs):
            ano_list = []
            for j in range(i+1, len(strs)):
                if Counter(strr) == Counter(strs[j]) and j not in map:
                    ano_list.append(strs[j])
                    map[j] = strs[j]

            if  i not in map:
                ano_list.append(strr)
                map[i] = strr   
            if ano_list:         
                big_list.append(ano_list)
        return big_list
