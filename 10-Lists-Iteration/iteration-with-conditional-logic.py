values = [3, 6, 9, 12, 58, 15, 18, 21, 24]


def odds_sum(numbers):
    result = 0
    for num in numbers:
        if num % 2 != 0:
            result += num
    return result


print(odds_sum(values))


def greatest_number(numbers):
    max_num = numbers[-1]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(greatest_number(values))
