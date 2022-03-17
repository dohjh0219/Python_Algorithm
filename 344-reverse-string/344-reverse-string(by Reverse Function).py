class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        
# Pythonic Way이다. reverse()가 아닌 슬라이싱으로도 문제 풀이가 가능하나 리트코드에서는 지원되지 않는다. 
# reverse() -> 리스트에서만 이용가능.
# 슬라이싱 -> 리스트 뿐만 아니라 문자열에서도 이용 가능.(리트코드에서는 리스트의 슬라이싱 지원X)
