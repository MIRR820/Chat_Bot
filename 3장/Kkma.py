# KoNLPy에서 제공하는 3가지 종류의 형태소 분석기

# KKma
from konlpy.tag import Kkma

#꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)
# NNG - 일반 명사, JKS - 주격 조사, JKM - 부사격 조사
# VV - 동사, EFN - 평서형 종결 어미, SF - 마침표, 물음표, 느낌표

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리    사용자가 여러 문장을 보낼때 유용하다.
sentences = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(sentences)
print(s)