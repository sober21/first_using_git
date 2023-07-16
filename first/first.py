def calc(a: int, b: int) -> int:
    return a * b


def two_calc(a: int) -> int:
    return a * 2


if __name__ == '__main__':
    print(two_calc(calc(10, 54)))
