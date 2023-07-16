def calc(a: int, b: int) -> int:
    return a * b


def two_calc(a: int) -> int:
    return a * 2


def int_for_str(a: int) -> str:
    return str(a)


if __name__ == '__main__':
    print(two_calc(calc(10, 54)))
    print(type(int_for_str(4)))
