# 반례 처리하다 GG 치고 방법을 바꿨다.
# 기존의 클래스 자료형은 유지한채로 DFS 알고리즘을 사용하기로 한다.
# 아무래도 물린거 같다
# 근데 여기서 DFS 쓰면 시간복잡도 n^3인데?
# 망했네 시팔
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
        pass

    def getLocSize(self):
        lsize = {}
        for loc, oils in self.loc.items():
            lsize[loc] = sum([self.size[i] for i in oils])
        return lsize


def solution(land):
    answer = 0
    # oils =
    chunks = OilChunks(land[0])
    key = 1

    # 여기 DFS같은거 넣으면 3중 반복문됨
    for r in range(len(land)):
        for c in range(len(land[r])):
            if land[r][c]:
                if (r, c) not in chunks.oils.keys():
                    chunks.newChunk((r,c), key)
                else:
                    chunks.loc[c].add(chunks.oils[(r,c)])


    print(chunks.loc)
    print(chunks.oils)
    result = max(chunks.getLocSize().values())

    return result