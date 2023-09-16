from sympy import mod_inverse

# 1. Выбор простых чисел
p = int(input("Введите первое простое число: "))
q = int(input("Введите второе простое число: "))

# 2. Вычисление модуля RSA и функции Эйлера
n = p * q
phi_n = (p-1) * (q-1)

# 3. Выбор открытой экспоненты
e = int(input("Введите открытую экспоненту (число, которое от 1 до " + str(phi_n) +" и взаимно простое с " + str(phi_n) + "): "))

# 4. Вычисление секретной экспоненты
d = mod_inverse(e, phi_n)

# Функция для шифрования сообщения с помощью RSA
def encrypt_rsa(message, e, n):
  return [pow(ord(char), e, n) for char in message]

# Функция для расшифровки сообщения с помощью RSA
def decrypt_rsa(encrypted, d, n):
  return ''.join([chr(pow(c, d, n)) for c in encrypted])

message = input("Введите инициалы или сообщение для шифрования: ")

# 5. Использование RSA для шифрования и дешифрования инициалов
encrypted = encrypt_rsa(message, e, n)
print('Зашифрованные данные:', encrypted)
decrypted = decrypt_rsa(encrypted, d, n)
print('Расшифрованные данные:', decrypted)
