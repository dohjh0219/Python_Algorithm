class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit():  # isdigit()을 이용하여 숫자 여부 판별.
                digits.append(log)  # 분석하고 있는 log가 숫자로 시작한다면 digits 리스트에 추가.(logs를 for로 돌리고 있으므로 logs가 순서대로 저장됨.)
            else:
                letters.append(log)  # 분석하고 있는 log가 숫자로 시작하지 않는다면 letters 리스트에 추가.
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # letters는 그냥 분석 순서대로 추가되어 있으므로 조건에 맞게 수정해야 함. 그렇기 때문에 sort함수를 사용함과 동시에  lambda를 이용하였다. 
        # sort하는데 있어서 key값을 split한 문자열 중 식별자를 제외한 나머지 부분을 기준으로 먼저 sort한다. 식별자를 제외한 나머지 부분이 동일할 경우 식별자 순으로 해야하므로 후차적으로 식별자를 기준으로 sort한다. 
        
        
        return letters + digits
