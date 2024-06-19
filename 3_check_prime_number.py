user_input = int(input('Введите число: '))

def check_prime(number):
    if user_input <= 0:
        return 'Число должно быть положительным'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(check_prime(user_input))