class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:  # 투 포인터가 찍은 윈도우가 펠린드롬일 경우, 확장하는 함수를 사용.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        if len(s) < 2 or s==s[::-1]:  # 해당 사항이 없을 때 그 자체를 리턴시키는 역할. [::-1]은 뒤집는 의미.
            return s
        
        result=''
        
        for i in range(len(s)-1):  # 한 칸씩 포인터를 옮기면서 펠린드롬인지 확인.
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)  # result는 그 전에 앞서 리턴된 펠린드롬 값, expand(i,i+1)은 2칸 포인터, expand(i,i+2)는 3칸 포인터. 그 중에서 길이가 가장 긴 펠린드롬을 result로 저장.
        
        return result
