'''
    프로그래머스 Level 1 문제 : '신규 아이디 추천'
    - 2021년 카카오 블라인드 채용 기출문제
    - 문제 푼 당일 기준 푼 사람 38,465명, 정답률 50%
    - 파이썬 문자열 자료형을 잘 다루는 것이 관건
    - 뭔가 지문이 길지만 지문에 단계별 설명이 잘되어 있기에 순차적으로 코딩하면 무난한 문제
'''
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    print(new_id)

    # 2단계
    newnew_id = ''
    for l in new_id:
        if l.isdigit() or l in ('abcdefghijklmnopqrstuvwxyz') or l in ('-', '_', '.'):
            newnew_id += l
    new_id = newnew_id
    print(new_id)

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    print(new_id)

    # 4단계
    while new_id[0] == '.':
        new_id = new_id[1:]

    while new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    print(new_id)

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:16]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    print(new_id)

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) >= 3:
            new_id += new_id[-1]
    print(new_id)

    return new_id

solution("=.=")