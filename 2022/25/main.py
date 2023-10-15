

NORMAL_DIGITS = "0123456789"
NORMAL_BASE = 10
NORMAL_START = 0

SNAFU_DIGITS = "=-012"
SNAFU_BASE = 5
SNAFU_START = -3

def to_normal(num: int) -> str:
    next_num = num // NORMAL_BASE
    last_digit = num % NORMAL_BASE
    result = NORMAL_DIGITS[last_digit + NORMAL_START]

    while next_num > 0:
        last_digit = next_num % NORMAL_BASE
        next_num = next_num // NORMAL_BASE
        result = NORMAL_DIGITS[last_digit + NORMAL_START] + result

    return result

def to_snafu(num: int) -> str:
    next_num = num // SNAFU_BASE
    last_digit = num % SNAFU_BASE
    result = SNAFU_DIGITS[last_digit + SNAFU_START]

    while next_num > 0 or last_digit >= abs(SNAFU_START):
        if last_digit >= abs(SNAFU_START):
            next_num += 1
        last_digit = next_num % SNAFU_BASE
        next_num = next_num // SNAFU_BASE
        result = SNAFU_DIGITS[last_digit + SNAFU_START] + result

    return result


def from_snafu(input: str) -> int:
    idx = len(input) - 1
    i = 0
    result = 0
    while idx >= 0:
        char = input[idx]
        digit = 0
        if char == '=':
            digit = -2
        elif char == '-':
            digit = -1
        elif char == '0':
            digit = 0
        elif char == '1':
            digit = 1
        elif char == '2':
            digit = 2
        result += digit * (SNAFU_BASE ** i)
        i += 1
        idx -= 1

    return result

def test():
    import random

    for _ in range(0, 6000):
        i = random.randint(0, 1234567890)
        assert i == int(to_normal(i)) == from_snafu(to_snafu(i))

if __name__ == '__main__':
    # test()
    with open("input.txt", "r") as input_file:
        snafu_nums = input_file.readlines()

    trimmed_snafus = map(lambda s: s.strip(), snafu_nums)
    converted_snafus = list(map(from_snafu, trimmed_snafus))
    total = sum(converted_snafus)
    print(to_snafu(total))
