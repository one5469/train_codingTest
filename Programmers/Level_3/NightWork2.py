'''
    프로그래머스 Level 3 문제 : '야근 지수'
    - 처음 풀어본 Level 3 문제. 정답률 자체는 높은편
    - 하필 주제가 야근이라니
    - 근무시간 만큼 순회하며 숫자를 줄이는 식으로 접근함
    - 결과를 산출하는데 람다 함수 사용
    - 테스트케이스는 모두 통과했으나 효율성 테스트에서 불통
'''
def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return answer

    max_idx = works.index(max(works))
    for i in range(n):
        works[max_idx] -= 1
        if works[max_idx] < max(works):
            max_idx = works.index(max(works))

    answer = sum(map(lambda x: x ** 2, works))

    return answer