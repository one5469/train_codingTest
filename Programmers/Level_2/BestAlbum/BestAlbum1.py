'''
    프로그래머스 Level 2 문제 : '베스트앨범'
    - 프로그래머스 알고리즘 kit에 '해시' 분류에 포함되어 있음
    - 해시는 key와 value를 이용한 자료구조
    - 파이썬에는 이를 구현할 수 있는 dictionary라는 훌륭한 자료형이 있다.
    - 장르별로 가장 많이 재생된 노래를 2개씩 뽑아 순서대로 인덱스를 반환한다.
    - 판다스 데이터프레임을 이용하면 아주 쉽게 풀거 같지만 외부 라이브러리를 사용하는 얍삽한 짓은 하지 않았다.
'''
# 테스트케이스 통과 실패. 중복도니 재생 횟수가 있는 것으로 보임
def solution(genres, plays):
    answer = []
    song_dict = {}
    total_play_dict = {}        # 장르별 총 재생 횟수를 담는 딕셔너리
    r_total_play_dict = {}      # 총 재생 횟수 반전 딕셔너리

    # 딕셔너리 제작
    for g, p in zip(genres, plays):
        if g in song_dict.keys():
            song_dict[g].append(p)
            total_play_dict[g] += p
        else:
            song_dict[g] = [p]
            total_play_dict[g] = p

    # 반전된 딕셔너리 제작
    for k, v in total_play_dict.items():
        r_total_play_dict[v] = k

    # 정답을 반환하기 위한 구문
    while len(r_total_play_dict) > 0:
        max_played = r_total_play_dict.pop(max(r_total_play_dict.keys()))
        play_list = song_dict[max_played]
        # 정답 리스트에 인덱스 추가
        answer.append(plays.index(play_list.pop(play_list.index(max(play_list)))))
        if len(play_list) > 0:
            answer.append(plays.index(max(play_list)))

    return answer