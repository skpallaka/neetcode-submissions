class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input : List of strings
        # Output : List of list of anagrams
        # Goal : Group words taht are anagrams and resturn them as a list
        
        # Sort strs alphabetically for each string using LIST COMPREHENSION
        sort_strs =  ["".join(sorted(word)) for word in strs]
        # Zip strs and sorted_strs together
        strs_zip = zip(sort_strs, strs)
        #empty dict
        anagram_dict = {}
        # We want to go through zipped list and find anagrams and sort by key value pairs
        for key, value in strs_zip :
            group_list = anagram_dict.get(key,[])
            group_list.append(value)
            anagram_dict[key] = group_list
        return list(anagram_dict.values())


        