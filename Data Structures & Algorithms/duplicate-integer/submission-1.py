class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico = {}
        for i in nums:
            if i in dico:
                return True
            else:
                dico[i]=True
        return False

            
        