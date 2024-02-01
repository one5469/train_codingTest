'''
    프로그래머스 Level 2 문제 : '문자열 압축'
    - 2020년 카카오 블라인드 채용 기출문제
    - 일정 개수로 문자열을 끊어 문자열을 압축할 때 가장 작은 길이 반환하기
    - 스택을 이용해서 풀이
    - 응 카카오 좆밥쉐키
'''
def solution(s):
    answer = 0

    min_len = 10000
    for leng in range(1, len(s) + 1):
        stack = []
        idx = 1
        while leng * idx < len(s) + 1:
            if len(stack) == 0:
                stack.append(s[leng * (idx - 1):leng * idx])
                idx += 1
            else:
                if stack[-1] == s[leng * (idx - 1):leng * idx]:
                    last = stack.pop()
                    if len(stack) > 0 and type(stack[-1]) == type(0):
                        stack[-1] += 1
                        stack.append(last)
                    else:
                        stack.append(2)
                        stack.append(last)
                    idx += 1
                else:
                    stack.append(s[leng * (idx - 1):leng * idx])
                    idx += 1
        if len(s[leng * (idx - 1):]) > 0:
            stack.append(s[leng * (idx - 1):])

        new_str = ''.join(map(str, stack))
        if len(new_str) < min_len:
            min_len = len(new_str)

    answer = min_len

    return answer