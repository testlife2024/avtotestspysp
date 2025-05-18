n = int(input('Введите число '))


def is_year_leap(n: int):
    if n % 4:
        return False
    else:
        return True


year_num = is_year_leap(n)
print(f'год {n}: {year_num}')

