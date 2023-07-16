def multiply(a: int, b: int) -> int:
    return a * b


def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def divide(a: int, b: int):
    if b == 0:
        return 'Деление на 0 невозможно'
    return a / b


if __name__ == '__main__':
    print(multiply(10, 54))
    print(divide(0, 4))
