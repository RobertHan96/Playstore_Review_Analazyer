from konlpy.tag import Okt
okt = Okt()

test = okt.morphs("아버지 가방에 들어가신다, 카트라이더 짱")

print(test)