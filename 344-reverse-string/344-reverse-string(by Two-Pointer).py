class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
            
# Two-Pointer : 2개의 포인터를 이용해 범위를 조정하여 풀이하는 방식.
