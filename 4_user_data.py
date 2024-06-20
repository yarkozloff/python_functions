# pip install tabulate
from tabulate import tabulate

users_dict = {}

# 1. Get data
def function_list_users(user_data):
    while True:
        # handling first_name (value)
        first_name = input("Введите имя: ")
        if first_name == "":
            break
        if not first_name.isalpha() or not first_name.istitle():
            first_name = first_name.capitalize()
        else:
            first_name = "NoFirstName"

        # handling last_name (value)
        last_name = input("Введите фамилию: ")
        if last_name == "":
            break
        if not last_name.isalpha() or not last_name.istitle():
            last_name = last_name.capitalize()
        else:
            last_name = "NoLastName"

        # handling age (value)
        age = input("Введите возраст: ")
        if age == "":
            break
        while not age.isdigit() or not 18 <= int(age) <= 60:
            print("Возраст должен быть числом от 18 до 60.")
            age = input("Введите возраст пользователя: ")

        # handling age (key)  
        user_id = input("Введите ID: ")
        while not user_id.isdigit() or len(user_id) > 8:
            print("ID должен иметь длину не более 8 знаков.")
            user_id = input("Введите ID пользователя: ")
        user_id = user_id.zfill(8)
        if user_id in users_dict:
            print("Пользователь с таким ID уже существует")
        else:
            users_dict[user_id] = (first_name, last_name, int(age))
        
        user_data[user_id] = (first_name, last_name, int(age))
    return user_data

# 2. Print Table
def print_table(user_data):
        table_data = [[key] + list(value) for key, value in user_data.items()]
        users_table = tabulate(table_data, headers=['ID', 'Имя', 'Фамилия', 'Возраст'], tablefmt='grid')
        return users_table


user_data = {}
user_data = function_list_users(user_data)
print(user_data)
        
print(print_table(user_data))