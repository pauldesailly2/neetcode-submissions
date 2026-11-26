class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #this first step avoid too much complexity for nothing
        if len(s)!= len(t):
            return False
        dic_s, dic_t = {},{}
        for letters in s:
            if letters in dic_s:
                dic_s[letters]+=1
            else :
                dic_s[letters]=1
        for letters in t:
            if letters in dic_t:
                dic_t[letters]+=1
            else :
                dic_t[letters]=1
        if dic_s == dic_t:
            return True
        return False

        

        