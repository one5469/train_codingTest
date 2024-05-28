'''
    프로그래머스 Level 2 문제 : '베스트앨범'
    - 프로그래머스 알고리즘 kit에 '해시' 분류에 포함되어 있음
    - 해시는 key와 value를 이용한 자료구조
    - 파이썬에는 이를 구현할 수 있는 dictionary라는 훌륭한 자료형이 있다.
    - 장르별로 가장 많이 재생된 노래를 2개씩 뽑아 순서대로 인덱스를 반환한다.
    - 판다스 데이터프레임을 이용하면 아주 쉽게 풀거 같지만 외부 라이브러리를 사용하는 얍삽한 짓은 하지 않았다.
'''
# 중복된 재생횟수가 있는게 핵심이였다.
# 중복된 재생횟수가 있을 경우 낮은 인덱스를 반환해야한다.
# 해당 반례를 처리하니 통과했다.
def solution(genres, plays):
    answer = []
    song_dict = {}
    total_play_dict = {}
    r_total_play_dict = {}

    # 밸류값에 들어가는 자료형을 리스트로 바꾸었다.
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g in song_dict.keys():
            if p in song_dict[g].keys():
                song_dict[g][p].append(idx)
            else:
                song_dict[g][p] = [idx]
            total_play_dict[g] += p
        else:
            song_dict[g] = {p: [idx]}
            total_play_dict[g] = p

    for k, v in total_play_dict.items():
        r_total_play_dict[v] = k

    while len(r_total_play_dict) > 0:
        max_played = r_total_play_dict.pop(max(r_total_play_dict.keys()))
        play_list = song_dict[max_played]
        print(play_list)

        if len(play_list[max(play_list.keys())]) > 1:
            answer.append(play_list[max(play_list.keys())][0])
            answer.append(play_list[max(play_list.keys())][1])
        else:
            answer.append(play_list.pop(max(play_list.keys()))[0])
            if len(play_list) > 0:
                answer.append(play_list[max(play_list.keys())][0])

    return answer