def my_sqrt(x: int) -> int:
    """
    Учитывая неотрицательное целое число x, вычислите и верните
    квадратный корень из x.
    Поскольку тип возвращаемого значения является целым числом,
    десятичные цифры усекаются, и возвращается только целая часть результата.
    Примечание. Вам не разрешается использовать какие-либо встроенные функции
    или операторы экспоненты, такие как pow(x, 0,5) или x ** 0,5.

    Example 1:
    Input: x = 4
    Output: 2

    Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part
    is truncated, 2 is returned.
    """
    left = 0
    right = x
    answer = 0
    while left <= right:
        middle = left + (right - left) // 2
        if middle * middle == x:
            return middle
        elif middle * middle < x:
            answer = middle
            left = middle + 1
        else:
            right = middle - 1
    return answer


print(my_sqrt(8))
