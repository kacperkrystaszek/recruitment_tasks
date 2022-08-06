WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def pesel_validation(pesel: str) -> bool:
    check_sum = 0
    for digit, weight in zip(pesel, WEIGHTS):
        check_sum += int(digit) * weight
    if 10 - check_sum % 10 == int(pesel[-1]):
        return True
    return False
