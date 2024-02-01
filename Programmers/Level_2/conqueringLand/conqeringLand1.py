'''
    프로그래머스 Level 2 문제 : '땅따먹기'
    - 4개 행과 n개의 열로 이루어진 이중 리스트가 주어짐
    - 같은 행을 두번 연속 밟지 않고 내려갈 때 가장 큰 점수 반환
    - 전형적인 동적 계획법 문제
    - 아래 코드같이 탐욕법 방식이 들어가 있으면 반례에 걸림
    - 아니 근데 애들 코드 왤캐 짧냐
'''

from copy import deepcopy

value_dict = {}
max_path_dict = {}
def solution(land):
    row_idx = 0

    while row_idx < len(land) - 1:
        for c in range(0, 4):
            next_land = deepcopy(land[row_idx + 1])
            value_dict[(row_idx, c)] = land[row_idx][c]
            max_path_dict[(row_idx, c)] = []
            next_land[c] = -1
            max_value = max(next_land)

            if next_land.count(max_value) == 1:
                max_path_dict[(row_idx, c)].append((row_idx+1, next_land.index(max_value)))
            else:
                for nc in range(0, 4):
                    if next_land[nc] == max_value:
                        max_path_dict[(row_idx, c)].append((row_idx+1, nc))

        row_idx += 1

    for c in range(0, 4):
        value_dict[(row_idx, c)] = land[row_idx][c]

    print(value_dict)
    print(max_path_dict)

    max_path = findMaxPath(len(land)-1)

    return max_path

def findMaxPath(limit):
    path1 = findNextPath((0, 0), limit)
    path2 = findNextPath((0, 1), limit)
    path3 = findNextPath((0, 2), limit)
    path4 = findNextPath((0, 3), limit)

    return max(path1, path2, path3, path4)

def findNextPath(loc, limit):
    if loc[0] == limit:
        return value_dict[loc]
    else:
        max_value = -1
        for next in max_path_dict[loc]:
            next_value = findNextPath(next, limit)
            if next_value > max_value:
                max_value = next_value
        return max_value + value_dict[loc]
