class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anaram has same characters as othe rword so same length but order is differenr
        return sorted(s) == sorted(t)