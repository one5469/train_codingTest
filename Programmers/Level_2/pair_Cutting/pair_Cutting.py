'''
    프로그래머스 Level 2 문제 : '짝찌어 제거하기'
    - 문자열이 입력됬을 때 2개로 짝지어진 문자를 차례로 제거하기
    - 문자열을 전부 제거하면 1로 반환, 아니면 0으로 반환
    - 분할 정복으로 해결하려 했는데 실패
'''

def solution(s):
    result = divide(s[:len(s) // 2], s[len(s) // 2:])

    if len(result) > 0:
        return 0
    else:
        return 1


def divide(s1, s2):
    if len(s1) > 1:
        s1 = divide(s1[:len(s1) // 2], s1[len(s1) // 2:])
    if len(s2) > 1:
        s2 = divide(s2[:len(s2) // 2], s2[len(s2) // 2:])

    return merge(s1, s2)


def merge(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        try:
            while s1[-1] == s2[0]:
                s1 = s1.replace(s1[-1], '')
                s2 = s2.replace(s2[0], '')
        except IndexError:
            pass
        finally:
            return s1 + s2