class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map={}  # 딕셔너리 생성
        
        for i, num in enumerate(nums):  # 인덱스, 키값 모두 enumerate함수로 리턴받음.
            if target - num in nums_map:  # taget-num이 딕셔너리에 있는지 확인.
                return [nums_map[target - num], i]  # if문 만족하면 리턴.
            nums_map[num]=i  
