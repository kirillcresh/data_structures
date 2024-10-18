import numpy
import sys

sys.setrecursionlimit(5000)


def recursive_power(num, exponent):
    if exponent == 0:
        return 1
    else:
        return num * recursive_power(num, exponent - 1)


def fast_power(num, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = fast_power(num, exponent // 2)
        return half_power * half_power
    else:
        return num * fast_power(num, exponent - 1)


def fast_power_bit(base, exponent):
    result = 1
    current_power = base

    while exponent > 0:
        if exponent & 1:
            result *= current_power

        current_power *= current_power

        # Сдвигаем экспоненту вправо на 1 бит
        exponent >>= 1

    return result


def get_power_result(method, base, exponent):
    if method == "Обычный способ":
        return pow(base, exponent)
    if method == "Модуль numpy":
        return numpy.power(base, exponent)
    if method == "Рекурсивное возведение":
        return recursive_power(base, exponent)
    if method == "Быстрое возведение в степень":
        return fast_power(base, exponent)
    if method == "Быстрое побитовое возведение":
        return fast_power_bit(base, exponent)
