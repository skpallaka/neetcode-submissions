class Solution:
    #1) count each string in the list
    #2) set a delimter in between to show diff 
    #3) combine and smush and then send to decode function
# s is string in strs: len s  + delimter +s , repeat


    def encode(self, strs: List[str]) -> str:
        smush =[]
        for s in strs :
            len_s = len(s)
            combined = str(len_s) + "-" + s # typeerror
            smush.append(combined)
        return "".join(smush)
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        while i < len(s):
            fnd = s.find("-",i)
            length = int(s[i:fnd])
            start = fnd+1 
            end = start+ length 
            result.append(s[start:end])
            i = end
        return result
