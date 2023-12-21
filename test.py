import fasttext

model = fasttext.load_model("model_cooking_reptile.bin")
# predict = model.predict("크레스티드 게코의 먹이활동")
# predict = model.predict("크레스티드 게코의 전망에 대해서 알려줄레?")
# predict = model.predict("크레스티드 게코의 사육현황에 대해서 알려줄레?")
# predict = model.predict("크레스티드 게코의 사육현황에 대해서 설명해주세요.")
# predict = model.predict("크레스티드 게코의 신체구조에 대해서 알려주면 정말 좋을 거 같아")
# predict = model.predict("이름이 뭐야?")
# predict = model.predict("크레스티드 게코 물")
# predict = model.predict("크레 물")
# predict = model.predict("크레 사육현황이 어떻게")
# predict = model.predict("크레스티드 게코 물")
# predict = model.predict("크레스티드 게코 사육장")
# predict = model.predict("크레스티드 게코 사육장")
# predict = model.predict("크레스티드 게코 사육장은 어떻게 꾸미는게 좋아?")
# predict = model.predict("크레스티드 게코 사육환")
# predict = model.predict("크레 먹이 얼마 동안 굶어야 죽어?")
# predict = model.predict("크레는 물 얼마 동안 못마시면 죽어?")
# predict = model.predict("im ji hun")
# predict = model.predict("카푸치노 모프")
# predict = model.predict("릴리화이트가 뭐야")
# predict = model.predict("크레")
# predict = model.predict("신체")

text_arr = ['크레', '크레의 신체구조', '대해', '설명', '신체', '구조']

for i in text_arr:
    print(i)
    predict = model.predict(i)
    print(predict)



#

# # predict2 = model.predict("Why not put knives in the dishwasher?", k=5)
# # test = model.test("cooking.valid")
#

# # print(test)
