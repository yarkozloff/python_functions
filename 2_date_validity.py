#29.02.2000 -> True
#29.02.2001 -> False
#31.04.1962 -> False

user_input = (input('Введите дату через точку: '))

# If import datetime - Use try/except for solutions

def validate_date(user_input):
    # Разделение текста на слова
    temp_split = user_input.split('.')
    if len(temp_split) == 3:
        temp_split = [int(x) for x in temp_split]
        print(temp_split)
        if 1 <= temp_split[1] <= 12:
            check_year = temp_split[2] % 4 == 0 and (temp_split[2] % 100 != 0 or temp_split[2] % 400 == 0)
            check_days_in_month = [31, 29 if check_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if 1 <= temp_split[0] <= check_days_in_month[temp_split[1] - 1]:
                return True
        return False
    return False

print(validate_date(user_input))
