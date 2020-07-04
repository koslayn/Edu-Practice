def solution(n):
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman_str = ''
    digit_list = [int(i) for i in str(n)]
    factor_list = range(len(digit_list)-1, -1, -1)
    digit_list_full = []

    def split_digit(d, factor):
        result = []
        while d:
            if d == 1:
                result.append(1 * 10 ** factor)
                d -= 1
            elif d == 5:
                result.append(5 * 10 ** factor)
                d -= 5
            else:
                if d < 4:
                    result.append(1 * 10 ** factor)
                    d -= 1
                elif d == 4:
                    result.append(1 * 10 ** factor)
                    result.append(5 * 10 ** factor)
                    d -= 4
                elif d == 9:
                    result.append(1 * 10 ** factor)
                    result.append(10 * 10 ** factor)
                    d -= 9
                else:
                    result.append(5 * 10 ** factor)
                    d -= 5
        return result

    for d, factor in zip(digit_list, factor_list):
        digit_list_full.extend(split_digit(d=d, factor=factor ))

    for i in digit_list_full:
        roman_str += roman[i]

    return roman_str

print(solution(89))

assert solution(1) == 'I'
assert solution(4) == 'IV'
assert solution(6) == 'VI'
assert solution(14) == 'XIV'
assert solution(21) == 'XXI'
assert solution(89) == 'LXXXIX'
assert solution(91) == 'XCI'
assert solution(984) == 'CMLXXXIV'
assert solution(1000) == 'M'
assert solution(1889) == 'MDCCCLXXXIX'
assert solution(1989) == 'MCMLXXXIX'


# for i, j in zip(digit_list, range(len(digit_list) - 1, -1, -1)):
#     print(i, j)
#     i = int(i)
#     if j == 3:
#         for _ in range(i):
#             digit_list_full.append(1000)
#     elif j == 2:
#         if i == 9:
#             digit_list_full.append(100)
#             digit_list_full.append(1000)
#             continue
#         if i >= 5:
#             digit_list_full.append(500)
#             i -= 5
#         for _ in range(i):
#             digit_list_full.append(100)
#     elif j == 1:
#         if i == 9:
#             digit_list_full.append(10)
#             digit_list_full.append(100)
#             continue
#         if i >= 5:
#             digit_list_full.append(50)
#             i -= 5
#         for _ in range(i):
#             digit_list_full.append(10)
#     else:
#         if i == 4:
#             digit_list_full.append(1)
#             digit_list_full.append(5)
#             continue
#         if i >= 5:
#             digit_list_full.append(5)
#             i -= 5
#         for _ in range(i):
#             digit_list_full.append(1)