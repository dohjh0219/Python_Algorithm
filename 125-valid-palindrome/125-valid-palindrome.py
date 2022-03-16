class Solution:
    def isPalindrome(self, s:str) -> bool:
        strs=[]
    
        for char in s:
            if char.isalnum():   # isalnum()은 영문자, 숫자 여부를 판별하는 함수. 공백, 특수문자 등 제외시키는 역할.
                strs.append(char.lower())  # 대소문자를 구별하지 않으므로 lower() 함수로 전원 소문자로 변환.

        while len(strs)>1:  # Palindrome 판별 시작
            if strs.pop(0) != strs.pop():
                return False

        return True
        