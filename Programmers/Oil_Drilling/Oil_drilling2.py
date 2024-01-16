# 클래스를 재정의해서 풀이 시도
# 클래스를 여러개 선언해서 리스트에 담지 않고 하나의 클래스 안에 석유 정보를 담음
# 시간 효율성 문제는 해결
# 하지만 개같이 실패 => 반례 있음 : 주변 석유 찾는 알고리즘과 병합 알고리즘 개선 필요
class OilChunks:
    def __init__(self, land):
        self.oils = {}
        self.loc = { i:set() for i in range(len(land)) }
        self.size = {}

    def newChunk(self, oil, key):
        self.oils[oil] = key
        self.loc[oil[1]].add(key)
        self.size[key] = 1

    def checkAround(self, oil):
        x, y = oil
        if (x + 1, y) in self.oils.keys():
            return self.oils[(x + 1, y)]
        elif (x - 1, y) in self.oils.keys():
            return self.oils[(x - 1, y)]
        elif (x, y + 1) in self.oils.keys():
            return self.oils[(x, y + 1)]
        elif (x, y - 1) in self.oils.keys():
            return self.oils[(x, y - 1)]
        else:
            return False

    def mergeOil(self, oil, chunk):
        self.oils[oil] = chunk
        self.loc[oil[1]].add(chunk)
        self.size[chunk] += 1

    def getLocSize(self):
        lsize = {}
        for loc, oils in self.loc.items():
            lsize[loc] = sum([self.size[i] for i in oils])
        return lsize


def solution(land):
    answer = 0
    chunks = OilChunks(land[0])
    key = 1

    for r in range(len(land)):
        for c in range(len(land[r])):
            if land[r][c]:
                oil = (r, c)
                chunk = chunks.checkAround(oil)
                if chunk:
                    chunks.mergeOil(oil, chunk)
                else:
                    chunks.newChunk(oil, key)
                    key += 1

    print(chunks.loc)
    print(chunks.oils)
    result = max(chunks.getLocSize().values())

    return result



print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]))