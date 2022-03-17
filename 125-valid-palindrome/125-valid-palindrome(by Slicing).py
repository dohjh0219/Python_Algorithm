class Solution:
    import re
    
    def isPalindrome(self, s:str) -> bool :
        s=s.lower() # 불필요한 문자 필터링

        s=re.sub('[^a-z0-9]','',s)  # 정규 표현식 문자열 치환을 통해서 불필요한 문자 필터링.

        return s==s[::-1]  # 문자열 슬라이싱을 통해 뒤집은 문자열 s와 같은지 비교 후 불리언으로 출력.
