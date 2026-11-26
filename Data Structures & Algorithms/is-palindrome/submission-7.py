class Solution:
    def isPalindrome(self, s: str) -> bool:
        liste = []
        for car in s:
            if car.isalnum():
                liste.append(car)
        for i in range(len(liste)//2):
            if liste[i].lower() != liste[len(liste)-i-1].lower():
                return False
        return True
