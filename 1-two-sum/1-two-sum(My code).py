class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        
        for i in range(len(nums)):  # 더하는 첫번째 숫자
            for j in range(i+1, len(nums)):  # 더하는 두번쨰 숫자
                if nums[i]+nums[j]==target:  # target과 같다면
                    result.append(i)  # i와 j를 각각 result 리스트에 추가.
                    result.append(j)
                    
        return result
