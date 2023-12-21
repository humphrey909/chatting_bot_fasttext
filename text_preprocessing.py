from konlpy.tag import Okt
Okt = Okt()

# sentence = '데이콘에서 다양한 컴피티션을 즐기면서 실력있는 데이터 분석가로 성장하세요!!.'
# sentence = '아잔틱 모프 추천해줘'
# sentence = '사육장추천해줘'
# sentence = '우성 열성이 뭐야?'
# sentence = '아잔틱 어떻게 구분해'
# sentence = '크레스티드 게코의 신체구조에 대해서 알려주면 정말 좋을 거 같아'
sentence = '크레의 신체구조에 대해서 설명해줘'


print("형태소 단위로 문장 분리")
print("----------------------")
print(Okt.morphs(sentence))

print(" ")
print("문장에서 명사 추출")
print("----------------------")
print(Okt.nouns(sentence))

print(" ")
print("품사 태킹(PoS)")
print("----------------------")
print(Okt.pos(sentence))

print(" ")
print("어절(phrases)")
print("----------------------")
print(Okt.phrases(sentence))


# import re
#
# tokenizer = Okt()
#
#
# def text_preprocessing(text, tokenizer):
#     stopwords = ['을', '를', '이', '가', '은', '는']
#
#     txt = re.sub('[^가-힣a-z]', ' ', text)
#     token = tokenizer.morphs(txt)
#     token = [t for t in token if t not in stopwords]
#
#     return token
#
#
# # ex_text = "이번에 새롭게 개봉한 영화의 배우들은 모두 훌륭한 연기력과 아름다운 목소리를 갖고 있어!!"
# ex_text = "사육장 하나만 수천해주라"
# example_pre = text_preprocessing(ex_text, tokenizer)
# print("example_pre")
# print("----------------------")
# print(example_pre)