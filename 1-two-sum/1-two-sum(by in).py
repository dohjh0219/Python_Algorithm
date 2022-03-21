class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, n in enumerate(nums):  # enumerate 함수는 입력받은 리스트 자료를 '인덱스 값, 데이터'를 리턴하는 함수이다. 그렇기 때문에 이 for문에서 i는 인덱스 값을, n은 그 인덱스에 해당하는 리스트 데이터를 리턴 받는다.
            complement = target - n  # complement에는 target값에서 n값을 뺀 데이터를 저장 받는다. 이후에 남은 nums 리스트에서 complement를 찾으면 조건에 해당하는 조합을 찾게되는 것이다.
            
            if complement in nums[i+1:]:  # 현재 for문으로 분석 중인 값의 인덱스가 i이므로 그 이후의 nums 리스트인 nums[i+1:]에 complement가 있는지 확인.
                return [nums.index(n), nums[i+1:].index(complement)+(i+1)]  # 있다면 nums 리스트에서 n값의 인덱스와, complement의 인덱스를 리턴.
