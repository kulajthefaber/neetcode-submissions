class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = dict()
        all_results = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            strs_dict[str(sorted_word)] = strs_dict.get(sorted_word,0) + 1
        
        for word in strs:
            results = []
            sorted_word = ''.join(sorted(word))
            for wword in strs:
                sorted_wword= ''.join(sorted(wword))
                if sorted_word == sorted_wword:
                    results.append(wword)
            
            if results and results not in all_results:
                all_results.append(results)


        return all_results

