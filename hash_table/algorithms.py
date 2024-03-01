def boyer_moore_search(main_string: str, pattern: str):
    """
    >>> text = "Being a developer is not easy"
    >>> pattern = "developer"
    >>> boyer_moore_search(main_string, pattern)
    8
    >>> boyer_moore_search('text', '-')
    -1

    :param main_string:
    :param pattern:
    :return:
    """

    def build_shift_table(pattern: str):
        """Створити таблицю зсувів для алгоритму Боєра-Мура."""
        table = {}
        length = len(pattern)
        # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
        table.setdefault(pattern[-1], length)
        return table

    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(main_string) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and main_string[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(main_string[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1


def knut_morris_pratt_search(main_string: str, pattern: str):
    """
    >>> raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."
    >>> pattern = "алг"
    >>> knut_morris_pratt_search(raw, pattern)
    True

    :param main_string:
    :param pattern:
    :return:
    """

    def compute_lps(pattern: str):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


def rabin_karp_search(main_string: str, pattern: str):
    """
    >>> main_string = "Being a developer is not easy"
    >>> substring = "developer"
    >>> rabin_karp_search(main_string, substring)
    8
    >>> rabin_karp_search("test", " ")
    -1

    :param main_string:
    :param pattern:
    :return:
    """

    def polynomial_hash(s: str, base=256, modulus=101):
        """
        Повертає поліноміальний хеш рядка s.
        """
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1) % modulus
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value

    # Довжини основного рядка та підрядка пошуку
    substring_length = len(pattern)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == pattern:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
