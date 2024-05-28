def solution(arrayA, arrayB):
    answer = 0

    all_divisor_A, co_divisor_A = find_all_div(arrayA)
    all_divisor_B, co_divisor_B = find_all_div(arrayB)

    # print(all_divisor_A, co_divisor_A)
    # print(all_divisor_B, co_divisor_B)

    not_co_divisor_AB = (co_divisor_A - all_divisor_B) | (co_divisor_B - all_divisor_B)
    if len(not_co_divisor_AB) > 0:
        answer = max(not_co_divisor_AB)

    return answer


def find_all_div(array):
    all_div = set()
    co_div = set()

    for i, e in enumerate(array):
        divisor = [n for n in range(1, e + 1) if e % n == 0]
        if i == 0:
            co_div = set(divisor)
            all_div = set(divisor)
        else:
            all_div.update(divisor)
            co_div = co_div & set(divisor)

    return all_div, co_div