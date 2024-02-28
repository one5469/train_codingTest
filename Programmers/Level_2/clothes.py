'''
    프로그래머스 Level 2 문제 : '의상'
    - 프로그래머스 알고리즘 kit에 '해시' 분류에 포함되어 있음
    - 해시는 key와 value를 이용한 자료구조
    - 파이썬에는 이를 구현할 수 있는 dictionary라는 훌륭한 자료형이 있다.
    - 종류별로 여러 가지의 옷을 가지고 있고 이를 조합할 수 있는 경우의 수를 구해야 한다. 단, 하나의 종류의 옷은 한가지만 입을 수 있다.
    - 한가지 종류의 옷만 입어도 된다. 예를 들어 선글라스 하나만 껴도 하나의 경우의 수로 인정된다.
    - 그럼 나머진 벌거벗는건가
    - 하여간 여기 문제들은 정상적인 문제가 없다.
'''

def solution(clothes):
    answer = 0
    clothes_dict = {}       # 옷의 종류와 개수를 담는 딕셔너리
    comb_dict = {}          # 조합의 수를 담기 위한 딕셔너리. 메모이제이션을 위해 사용

    # 딕셔너리에 일단 옷들을 다 담는다.
    for c, k in clothes:
        if k in clothes_dict.keys():
            clothes_dict[k].append(c)
        else:
            clothes_dict[k] = [c]

    # 한가지 종류의 옷만 착용할 경우를 먼저 담는다.
    comb_dict[1] = [len(c) for c in clothes_dict.values()]
    answer += sum(comb_dict[1])

    # 동적 계획법 이용
    # 이전에 계산한 조합의 수를 이용해 다음 조합의 수를 계산한다.
    for num in range(2, len(clothes_dict) + 1):
        i = 0
        comb_dict[num] = []

        for i in range(0, len(comb_dict[num - 1]) - 1):
            comb_dict[num].append(sum(comb_dict[num - 1][i + 1:] * comb_dict[1][i]))
        answer += sum(comb_dict[num])

    return answer