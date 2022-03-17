class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
                
        words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]  # 뒤 부터 해석. banned에 포함되어 있지 않은 word라면, re.sub를 통해 Paragraph의 단어 문자가 아닌 모든 문자를 공백화.
        
        counts = collections.Counter(words)  # 문자열이나, list의 요소를 카운팅하여 많은 순으로 Dictionary 형태로 리턴.
        
        return counts.most_common(1)[0][0]  # 개수가 많은 순으로 정렬된 counts를 리턴.(이때 소괄호 안에 있는 숫자는 1개만 출력한다는 의미. 키만 가져오면 되므로 첫번째 [0]은 최대로 많이 쓰인 것. 두 번재 [0]은 키값.
        # 이 때 [0][0]이 없으면 그냥 딕셔너리 형태로 출력되므로 꼭 [0][0]을 기입할 것.
