import math


def binary_search(arr: list[float], x: float):
    """
    Функція для двійкового пошуку відсортованого масиву з дробовими числами.

    Параметри:
    arr (list): Відсортований масив.
    x (float): Шукане значення.

    Повертає:
    tuple: Кортеж з кількістю ітерацій та верхньою межею.
    """
    left = 0
    right = len(arr) - 1
    iterations = 0

    while abs(left - right) > 1:
        mid = left + (right - left) // 2
        iterations += 1

        # Якщо знайдено шукане значення, повертаємо результат
        if math.isclose(arr[mid], x):
            return iterations, arr[mid]

        # Якщо поточний елемент менший за шукане значення, зміщуємо ліву границю
        elif arr[mid] < x:
            left = mid
        # Якщо поточний елемент більший за шукане значення, зміщуємо праву границю
        else:
            right = mid

    # Якщо значення не знайдено, повертаємо останній елемент як верхню межу
    return iterations, arr[right]


# Приклад використання:
arr = [0.1, 0.5, 1.2, 2.5, 3.7, 4.8, 5.9, 6.3, 7.4, 8.6]
x = 0.2
iterations, upper_bound = binary_search(arr, x)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
