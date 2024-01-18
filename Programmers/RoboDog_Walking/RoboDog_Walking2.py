'''
    프로그래머스 Level 1 문제 : '공원 산책'
    - Level 2 푼다고 깝치다가 도망옴
    - Level 1 치곤 퀄리티와 난이도가 괜찮아보여 가져옴
'''
# 인덱싱을 안해서 논리 오류가 있었다
# 테스트케이스 통과
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
            if checkRange(dog[0], -(move), len(line)) and checkLine(line[dog[0]-move:dog[0]]):
                dog[0] -= move
        elif route[0] == 'S':
            line = getVertical(park, dog[1])
            if checkRange(dog[0], move, len(line)) and checkLine(line[dog[0]:dog[0]+move+1]):
                dog[0] += move
        elif route[0] == 'W':
            line = park[dog[0]]
            if checkRange(dog[1], -(move), len(line)) and checkLine(line[dog[1]-move:dog[1]]):
                dog[1] -= move
        elif route[0] == 'E':
            line = park[dog[0]]
            if checkRange(dog[1], move, len(line)) and checkLine(line[dog[1]:dog[1]+move+1]):
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


print(solution(["XXX", "XXS", "XXX", "XXX"], ["N 3", "S 2", "E 1"]))
print(solution(["OOOO", "OXSO", "XXOX", "XXXX"], ["N 3", "S 1", "N 2", "W 1", "E 2"]))
print(solution(["OXXXO", "XOSOX", "XOOOX", "XXXXX"], ["N 2", "S 4", "E 1", "W 1", "E 2", "N 1"]))
print(solution(["OO", "OO", "OO", "SO"], ["N 3", "S 2", "E 1"]))

