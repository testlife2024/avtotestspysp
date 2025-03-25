def month_to_season(name: int):
    if name == 1 or name == 2:
        print('Зима')
    elif 3 <= name <= 5:
        print('Весна')
    elif 6 <= name <= 8:
        print('Лето')
    else:
        print('Осень')


month = int(input())
month_to_season(month)
