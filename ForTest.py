from collections import deque as deq

class oilchunk:
    def __init__(self, oil):
        self.oil = [oil]
        self.loc = {oil[1]}
        self.boundry = {(oil[0] + 1, oil[1]), (oil[0] - 1, oil[1]),
                        (oil[0], oil[1] + 1), (oil[0], oil[1] - 1)}
        self.size = 1

    def mergeOil(self, oil):
        self.oil.extend(oil.oil)
        self.loc = self.loc.union(oil.loc)
        self.boundry = self.boundry.union(oil.boundry)
        self.size += 1

    def checkMerge(self, chunk):
        for o in chunk.oil:
            if o in self.boundry:
                return True
        return False

    def drilling(self, drill):
        for l in self.loc:
            drill[l] += self.size
        return drill


def solution(land):
    chunks = findOils(land)
    drill = {i:0 for i in range(len(land[0]))}

    for c in chunks:
        drill = c.drilling(drill)

    return max(drill.values())


def findOils(land):
    r, c = 0, 0
    oils = []

    while r < len(land):
        if land[r][c]:
            oil = oilchunk((r,c))
            if len(oils) != 0:
                toMerge = check(oils, oil)
                if toMerge == None:
                    oils.append(oil)
                else:
                    oils[toMerge].mergeOil(oil)
            else:
                oils.append(oil)

        c += 1
        if c >= len(land[r]):
            c = 0
            r += 1

    return oils


def check(chunks, oil):
    for c in chunks:
        if c.checkMerge(oil):
            return chunks.index(c)
    return None

solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])