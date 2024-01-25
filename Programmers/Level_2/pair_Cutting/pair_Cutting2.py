'''
    프로그래머스 Level 2 문제 : '짝찌어 제거하기'
    - 문자열이 입력됬을 때 2개로 짝지어진 문자를 차례로 제거하기
    - 문자열을 전부 제거하면 1로 반환, 아니면 0으로 반환
    - 사실 스택으로 풀면 되는 날먹 문제였음
    - 시발 존나 억울하네
'''
def solution(s):
    stack = []

    for l in s:
        if not stack or stack[-1] != l:
            stack.append(l)
        else:
            stack.pop()

    if len(stack) > 0:
        return 0
    else:
        return 1