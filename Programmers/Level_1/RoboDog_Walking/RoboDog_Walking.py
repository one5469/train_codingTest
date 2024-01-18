'''
    프로그래머스 Level 1 문제 : '공원 산책'
    - Level 2 푼다고 깝치다가 도망옴
    - Level 1 치곤 퀄리티와 난이도가 괜찮아보여 가져옴
'''
# 근데 생각보다 함수 정의가 많이 필요한디
# 테케 통과 실패
def solution(park, routes):
    answer = []

    for p in park:
        if 'S' in p:
            dog = [park.index(p), p.index('S')]  # (리스트 인덱스, 문자열 인덱스)
            break

    for route in routes:
        move = int(route[-1])
        if route[0] == 'N':
            line = getVertical(park, dog[1])
            if checkRange(dog[0], -(move), len(line)) and checkLine(line):
                dog[0] -= move
        elif route[0] == 'S':
            line = getVertical(park, dog[1])
            if checkRange(dog[0], move, len(line)) and checkLine(line):
                dog[0] += move
        elif route[0] == 'W':
            line = park[dog[0]]
            if checkRange(dog[1], -(move), len(line)) and checkLine(line):
                dog[1] -= move
        elif route[0] == 'E':
            line = park[dog[0]]
            if checkRange(dog[1], move, len(line)) and checkLine(line):
                dog[1] += move

    return dog


def checkRange(loc, gap, limit):
    if -1 < loc + gap < limit:
        return True
    else:
        return False


def checkLine(line):
    if 'X' in line:
        return False
    else:
        return True


def getVertical(park, index):
    string = ''
    for p in park:
        string += p[index]

    return string


print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
