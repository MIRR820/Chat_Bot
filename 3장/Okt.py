# KoNLPy에서 제공하는 3가지 종류의 형태소 분석기

# Okt 빅데이터에서 간단한 한국어 처리를 통해 색인어를 추출하는 목표를
# 가지고 있어 완전한 수준의 형태소 분석을 지향하지 않는다.
# 공식적으로 Okt를 한국어 처리기라 표현한다.

from konlpy.tag import Okt

# 형태소 처리기 객체 생성
okt = Okt()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)
# Noun - 명사, Verb - 동사, Adjective - 형용사, Josa - 조사, Punctuation - 구두점

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)

# 정규화, 어구 추출
text = "오늘 날씨가 좋아욬ㅋㅋ"
print(okt.normalize(text)) # 정규화
print(okt.phrases(text)) # 어구 추출