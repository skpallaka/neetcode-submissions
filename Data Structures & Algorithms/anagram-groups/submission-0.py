class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1) Sort alphabetically and check if equal
        2) count length of each string and check if equal(might be redundant tho)
        """
        sorted_strs = ["".join(sorted(word)) for word in strs]
        sip = zip( sorted_strs, strs) # sip = [("eat,"aet"),("tea,"aet"), ("tan,"ant")]
        my_dict = {}
        for key, value in sip:
            c_list = my_dict.get(key,[])
            c_list.append(value)
            my_dict[key] = c_list
        return list(my_dict.values())







        
