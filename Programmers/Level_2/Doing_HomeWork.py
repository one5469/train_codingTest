'''
    프로그래머스 Level 2 문제 : '과제 진행하기'
    - 시작 시간과 진행 시간이 주어진 과제 리스트가 주어지고 완료되는 과제순으로 반환하는 문제
    - 다음 과제 시작 시간이 되면 기존의 과제를 멈추고 다음 과제를 먼저 진행하며, 남은 과제 중에서 가장 나중에 수행했던 것을 먼저 수행함
    - 스택 자료구조를 이용해서 풀이할 수 있다.
'''

def solution(plans):
    answer = []
    stack = []  # 진행 중인 과제를 담기 위한 스택 정의

    # 시작 시간과 소요 시간을 정수형으로 변환
    for i in plans:
        start = i[1].split(":")
        i[1] = int(start[0]) * 60 + int(start[1])
        i[2] = int(i[2])

    # 과제를 시작 시간을 기준으로 정렬
    plans.sort(key=lambda x: x[1])

    stack.append(plans[0])
    clock = stack[-1][1]
    idx = 1

    # 과제 목록 순회
    while idx < len(plans):
        # print(stack)
        nextwork = plans[idx]

        # 스택이 비었을 경우 다음 과제를 저장
        if len(stack) == 0:
            clock = nextwork[1]
            stack.append(nextwork)
            idx += 1
            continue
        eta = clock + stack[-1][-1]
        # 과제 종료 시간이 다음 과제 시작 시간과 같을 때
        if eta == nextwork[1]:
            answer.append(stack[-1][0])
            stack.pop()
            stack.append(plans[idx])
            clock = nextwork[1]
            idx += 1
        # 과제 종료 시간이 다음 과제 시작 시간보다 작을 때
        elif eta < nextwork[1]:
            clock = eta
            answer.append(stack[-1][0])
            stack.pop()
            # 다음 과제 시작 시간까지 남아있는 과제 처리
            while len(stack) > 0:
                if clock + stack[-1][-1] < nextwork[1]:
                    clock += stack[-1][-1]
                    answer.append(stack[-1][0])
                    stack.pop()
                elif clock + stack[-1][-1] == nextwork[1]:
                    clock += stack[-1][-1]
                    answer.append(stack[-1][0])
                    stack.pop()
                    stack.append(plans[idx])
                    idx += 1
                    break
                else:
                    gap = nextwork[1] - clock
                    clock = nextwork[1]
                    stack[-1][-1] -= gap
                    stack.append(plans[idx])
                    idx += 1
                    break
        # 과제 종료 시간이 다음 과제 시작 시간보다 클 때
        elif eta > nextwork[1]:
            gap = nextwork[1] - clock
            clock = nextwork[1]
            stack[-1][-1] -= gap
            stack.append(plans[idx])
            idx += 1

    # print(stack)
    # 스택에 남아있는 과제 처리
    for rest in reversed(stack):
        answer.append(rest[0])
    return answer