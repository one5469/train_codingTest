'''
    프로그래머스 Level 3 문제 : '인사고과'
    - 인사 점수가 주어지고 리스트의 맨 앞에 주어진 영호의 석차를 맞추는 문제
    - 인사 점수의 종류는 두가지이고, 이 두 점수가 각각 자신보다 둘다 높은 사람이 있으면 석차에 포함되지 않는다.
    - 석차에 포함되지 않는 사람을 처리하는 부분이 핵심이다.
    - 문제 길이는 짧은 데 반례가 생각보다 많아 의외로 까다롭다.
'''

def solution(scores):
    answer = 0
    wanho = scores[0]   # 완호의 점수
    remove_list = []

    # 주어진 인사점수의 길이가 1일 때 바로 처리
    if len(scores) == 1:
        return 1

    # 완호가 석차에 포함되지 않을 때 처리
    for score in scores[1:]:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1

    # 리스트를 직접 이중 순회하며 비교하는 방식. 시간 복잡도가 O(n^2)이기에 시간 초과가 난다.
    # for idx in range(len(scores)):
    #     for score in scores:
    #         if scores[idx][0] < score[0] and scores[idx][1] < score[1]:
    #             remove_list.append(scores[idx])
    #             if idx == 0:
    #                 return -1

    # 순회 과정에서 조건을 추가한 방식. 실행 시간이 줄어들지만 역시 시간 초과가 난다.
    # for idx in range(len(scores)):
    #     for score in scores[idx+1:]:
    #         if scores[idx][0] < score[0] and scores[idx][1] < score[1]:
    #             remove_list.append(scores[idx])
    #         elif scores[idx][0] > score[0] and scores[idx][1] > score[1]:
    #             remove_list.append(score)

    # 단순 순회 방식에서는 시간 초과가 나기에 이를 해결하기 위해 첫번째 점수를 기준으로 리스트를 나누고, 각 카테고리별로 두번째 점수의 최대값을 저장.
    score_dict, max_dict = makeDict(scores)
    # print(score_dict, max_dict)
    max_key = -1

    # 현재 키를 이전 키들 값의 최대값과 비교하여 석차에 포함되지 않는 값 제거
    for key, value in score_dict.items():
        if max_key > -1:
            for v in value:
                if v < max_dict[max_key]:
                    scores.remove([key, v])
        max_key = key
        # print(scores)

    # 처리된 인사점수 리스트의 합을 추출하여 영호의 석차 계산
    totalScore = [sum(score) for score in scores]
    totalScore.sort(reverse=True)

    answer = totalScore.index(sum(wanho)) + 1

    return answer


# 첫번째 점수를 키로, 각각의 두번째 점수와 최대값 딕셔너리를 반환하는 함수
def makeDict(scores):
    scores.sort(reverse=True)

    result = {}
    max_dict = {}
    max = -1

    for score in scores:
        if score[0] in result.keys():
            result[score[0]].append(score[1])
        else:
            result[score[0]] = [score[1]]

        if score[1] > max:
            max_dict[score[0]] = score[1]
            max = score[1]
        elif score[0] not in max_dict.keys():
            max_dict[score[0]] = max

    return result, max_dict