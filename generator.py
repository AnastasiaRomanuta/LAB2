#базовая структура

import string
import random
#функции для генерации
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    #ввод и генерация
password_length = int(input("Введите желаемую длину пароля: "))
generated_password = generate_password(password_length)
print("Ваш сгенерированный пароль:", generated_password)
