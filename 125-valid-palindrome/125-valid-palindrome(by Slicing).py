class Solution:
    import re
    
    def isPalindrome(self, s:str) -> bool :
        s=s.lower() # 불필요한 문자 필터링

        s=re.sub('[^a-z0-9]','',s)

        return s==s[::-1]
