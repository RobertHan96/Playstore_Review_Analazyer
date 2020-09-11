# -*-coding:utf-8-*-
import json


class KnuSL():

    def data_list(wordname):
        with open('data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
            data = json.load(f)
        result = ['None', 'None']
        for i in range(0, len(data)):
            if data[i]['word'] == wordname:
                result.pop()
                result.pop()
                result.append(data[i]['word_root'])
                result.append(data[i]['polarity'])

        r_word = result[0]
        s_word = result[1]

        # print('어근 : ' + r_word)
        # print('극성 : ' + s_word)

        return s_word


if __name__ == "__main__":
    ksl = KnuSL
    # print("\nKNU 한국어 감성사전입니다~ :)")
    # print("사전에 단어가 없는 경우 결과가 None으로 나타납니다!!!")
    # print("종료하시려면 #을 입력해주세요!!!")
    # print("-2:매우 부정, -1:부정, 0:중립 or Unkwon, 1:긍정, 2:매우 긍정")
    # print("\n")

    total = 0
    test = {'게임': 41, '카트': 28, '티어': 22, '과금': 20, '유저': 19, '진짜': 18, '정말': 14, '현질': 14, '다이아': 12, '레전드': 11, '제발': 10, '업데이트': 10,
            '사람': 9, '시즌': 8, '단점': 8, '시간': 8, '전체': 8, '하나': 8, '버그': 7, '다시': 7, '핑코': 7, '유도': 7,
            '업': 5, '리뷰': 5, '건전지': 5, '채팅': 5, '플래티넘': 5, '랭킹': 4, '생각': 4, '기록': 4, '등등': 4, '마음': 4, '이벤트': 4, '살수': 4, '마스터': 4, '가지': 4, '시작': 4, '장점': 4}
    words = test.keys()
    for word in words:
        result = ksl.data_list(word)
        if result.isnumeric() == True:
            total += int(result)
            print(total)
