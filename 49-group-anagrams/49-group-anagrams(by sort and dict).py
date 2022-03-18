class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)  # 존재하지 않는 키를 삽입하려면 KeyError가 발생하므로 에러 제거를 위해 default 딕셔너리 생성.
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)  # 입력된 strs를 for문 시작하면서 word로 분석 시작. word를 sorted하고 나면 리스트 형태이므로 join으로 묶음. join 앞에 ''. 가 붙은 이유는 모든 리스트 element를 공백 없이 묶고자 함에 있다. 만약 [] 사이에 있는 원소가 'apple'로 완성이 되었으면, anagrams의 'apple' 키에 입력받은(분석중인) word를 추가 한다.
            
        return list(anagrams.values())  # anagram 딕셔너리의 값을 묶어 리스트 형태로 반환.
