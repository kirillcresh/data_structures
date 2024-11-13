import random


def divide(dividend: str, divisor: str) -> tuple[str, str]:
    if divisor == "0":
        raise ValueError("Деление на ноль невозможно")

    if int(dividend) < int(divisor):
        return "0", dividend

    quotient = ""
    current = "0"

    for digit in dividend:
        current = str(int(current + digit))

        multiple = 0
        while int(current) >= int(divisor) * (multiple + 1):
            multiple += 1

        quotient += str(multiple)
        current = str(int(current) - int(divisor) * multiple)

    quotient = quotient.lstrip("0")
    return quotient, current


def optimized_divide(dividend: str, divisor: str) -> tuple[str, str]:
    if divisor == "0":
        raise ValueError("Деление на ноль невозможно.")

    if int(dividend) < int(divisor):
        return "0", dividend

    quotient = []
    remainder = int(dividend[:len(divisor)])

    for i in range(len(divisor), len(dividend) + 1):
        q = remainder // int(divisor)
        quotient.append(str(q))

        remainder = remainder - q * int(divisor)
        if i < len(dividend):  # остаток
            remainder = remainder * 10 + int(dividend[i])

    return "".join(quotient).lstrip("0"), str(remainder)


def generate_long_number(length):
    return "".join(random.choices("123456789", k=length))
