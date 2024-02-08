'''
    프로그래머스 Level 3 문제 : '야근 지수'
    - 처음 풀어본 Level 3 문제. 정답률 자체는 높은편
    - 하필 주제가 야근이라니
    - 근무시간 만큼 순회하며 숫자를 줄이는 식으로 접근함
    - 결과를 산출하는데 람다 함수 사용
    - 테스트케이스는 모두 통과했으나 효율성 테스트에서 불통
    - 검사 결과 for문에서 연산 과부하가 걸리는 것으로 보임. 알고리즘 개선 필요
'''
def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return answer

    for i in range(n):
        max_idx = works.index(max(works))
        works[max_idx] -= 1

    answer = sum(map(lambda x: x ** 2, works))

    return answer