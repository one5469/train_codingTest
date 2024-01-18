from copy import deepcopy as dp

# 반례 해결하려 시도 중
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
        # if (x + 1, y) in self.oils.keys():
        #     return self.oils[(x + 1, y)]
        if (x - 1, y) in self.oils.keys():
            return self.oils[(x - 1, y)]
        # elif (x, y + 1) in self.oils.keys():
        #     return self.oils[(x, y + 1)]
        elif (x, y - 1) in self.oils.keys():
            return self.oils[(x, y - 1)]
        else:
            return False

    def checkMerge(self, chunk1, chunk2):
        chunk1_loc = [l for l, o in self.oils.items() if o == chunk1]
        chunk2_loc = [l for l, o in self.oils.items() if o == chunk2]
        for ch1r, ch1c in chunk1_loc:
            if (ch1r+1, ch1c) in chunk2_loc or (ch1r-1, ch1c) in chunk2_loc or (ch1r, ch1c+1) in chunk2_loc or (ch1r+1, ch1c-1) in chunk2_loc:
                return True
        return False


    def mergeOil(self, oil, chunk):
        self.oils[oil] = chunk
        self.loc[oil[1]].add(chunk)
        self.size[chunk] += 1

    def mergeChunk(self, chunk1, chunk2):
        newoils = dp(self.oils)
        for l, o in self.oils.items():
            if o == chunk2:
                newoils[l] = chunk1
        self.oils = newoils

        newlocs = dp(self.loc)
        for l, c in self.loc.items():
            if chunk1 in newlocs[l] and chunk2 in newlocs[l]:
                newlocs[l].remove(chunk2)
        self.loc = newlocs

        self.size[chunk1] += self.size[chunk2]
        self.size.pop(chunk2)

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



print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))