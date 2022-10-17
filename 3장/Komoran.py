# KoNLPy에서 제공하는 3가지 종류의 형태소 분석기

# Komoran   공백이 포함된 형태소 단위로도 분석이 가능하다.
from konlpy.tag import Komoran

# 코모란 형태소 분석기 객체 생성
komoran = Komoran()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = komoran.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(pos)
# NNG - 일반 명사, JKS - 주격 조사, JKB - 부사격 조사
# VV - 동사, EF - 종결 어미, SF - 마침표, 물음표, 느낌표

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
