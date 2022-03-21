class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map={}  # 딕셔너리 생성.
        
        for i, num in enumerate(nums):  # 인덱스와 키 값 동시 리턴하는 enumerate 함수 이용.
            nums_map[num]=i  # 딕셔너리를 '키 값, 인덱스 값' 순으로 저장.
            
        for i, num in enumerate(nums):  # 인덱스와 키 값 동시 리턴하는 enumerate 함수 이용.
            if target - num in nums_map and i != nums_map[target - num]:  # 위 딕셔너리에서 target-num 값이 있는지 확인. 동시에 같은 딕셔너리를 찾을 경우를 제외해야 하므로 and로 조건 교집합.
                return [i, nums_map[target - num]] # if문 만족하면 리턴.
