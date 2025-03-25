def fizz_buzz(n: int):
    for i in range(1,n):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        else:
            print(i)



#я не понимаю почему он печатает
# None после работы программы
n = int(input())
print(fizz_buzz(n))
