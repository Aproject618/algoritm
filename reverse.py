'''
Для 32-битного целого числа x со знаком вернуть x с перевернутыми цифрами. 
Если реверсирование x приводит к тому, что значение выходит за пределы 
диапазона 32-битных целых чисел со знаком [-2 ** 31, 2 ** 31 - 1], возвращается 0.

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer
range [-2 ** 31, 2 ** 31 - 1], then return 0.

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

'''
def reverse(x):

    if x >= 0:
        x = str(x) # Преобразуем тип int() в тип str()
        x = int(x[::-1]) # Переворачиваем строку и преобразуем тип str() в тип int()

    else:
        x = str(x) # Преобразуем тип int() в тип str()
        x = x[1:] # Отсекаем знак "-"
        x = int(x[::-1]) * - 1 # Переворачиваем строку и преобразуем тип str() в тип int() возвращаем знак "-"

    if -2147483648 < x < 2147483647: # Делаем проверку на допустимый диапазон
        return x

    else:
        return 0
             
def reverse_2(x):
    answer = ''
    if x > 0:

        while x != 0:

            pop = x % 10 # Получаем последнее число
            x = x // 10 # Отрезаем последнее число
            answer += str(pop) # Конкатенируем ответ
        answer = int(answer) # Преобразуем тип str() в int()

    elif x < 0 :

        x = x * - 1 # Тоже, что и выше, только изначально отбрасываем минус
        while x != 0:
            pop = x % 10
            x = x // 10
            answer += str(pop)
        answer = int(answer) * - 1

    else:
        return 0

    if -2147483648 < answer < 2147483647: # Делаем проверку на допустимый диапазон
        return answer
        
    else:
        return 0             

print(reverse(123))
print()
print(reverse(-321))
print()
print(reverse(12345465466789))
print()
print(reverse(0))
print()
print(reverse_2(132))
print()
print(reverse_2(-321))
print()
print(reverse_2(12345465466789))
print()
print(reverse(0))
