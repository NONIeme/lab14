# Лабораторна робота №14: Робота з логічними операціями у Python

## Мета роботи
Метою даної лабораторної роботи є закріплення навичок використання логічних операцій та умовних виразів у Python, а також реалізація різноманітних задач, пов'язаних з логічними умовами та операторами.

## Опис завдання
1. **check_truth(a, b, c)**: Перевірка істинності виразу `(a and b) or c`.
2. **logical_equivalence(a, b)**: Перевірка логічної еквівалентності двох значень.
3. **xor(a, b)**: Реалізація логічного виключного АБО (XOR).
4. **greet(boolean_value)**: Повернення "Hello, World!" якщо значення істинне, інакше "Goodbye, World!".
5. **nested_condition(x, y, z)**: Перевірка трьох значень на рівність або різність.
6. **count_true(boolean_list)**: Підрахунок кількості істинних значень у списку.
7. **parity(integer)**: Перевірка парності кількості одиниць у двійковому представленні числа.
8. **majority_vote(a, b, c)**: Повернення більшості голосів серед трьох значень.
9. **switch(boolean_value)**: Перемикання значення на протилежне.
10. **ternary_check(condition, result_if_true, result_if_false)**: Реалізація тернарного оператора.
11. **validate(x, y, z)**: Перевірка комбінації логічних умов.
12. **chain_check(a, b, c)**: Перевірка на зростання або спадання трьох значень.
13. **filter_true(boolean_list)**: Фільтрація істинних значень у списку.
14. **multiplexer(a, b, c, integer)**: Реалізація умовного мультиплексора.

## Виконання роботи
### Кроки виконання
1. Кожна лабораторна робота повинна бути завантажена в окрему папку на GitHub.
2. Назва папки повинна містити номер лабораторної роботи (наприклад, `lab14`).
3. В кожній папці повинні бути присутні наступні файли:
   - Основний код програми (`main.py`).
   - README файл з детальним поясненням.

### Структура проекту
lab14
-├── student_main.py
-├── README.md

### Опис файлів
- **main.py**: Основний код програми, що містить визначення всіх функцій.
- **README.md**: Файл з детальним поясненням.

### Опис основних функцій
- **check_truth(a, b, c)**: Повертає результат логічного виразу `(a and b) or c`.
- **logical_equivalence(a, b)**: Повертає `True`, якщо `a` та `b` еквівалентні, інакше `False`.
- **xor(a, b)**: Повертає `True`, якщо одне з значень `a` або `b` істинне, але не обидва.
- **greet(boolean_value)**: Повертає "Hello, World!", якщо значення істинне, інакше "Goodbye, World!".
- **nested_condition(x, y, z)**: Повертає "All same", якщо всі значення рівні, "All different" якщо всі різні, інакше "Neither".
- **count_true(boolean_list)**: Повертає кількість істинних значень у списку.
- **parity(integer)**: Повертає `True`, якщо кількість одиниць у двійковому представленні числа парна, інакше `False`.
- **majority_vote(a, b, c)**: Повертає `True`, якщо більшість значень істинні.
- **switch(boolean_value)**: Повертає протилежне значення.
- **ternary_check(condition, result_if_true, result_if_false)**: Повертає `result_if_true` якщо умова істинна, інакше `result_if_false`.
- **validate(x, y, z)**: Повертає результат логічного виразу `x or (y and z)`.
- **chain_check(a, b, c)**: Повертає "Increasing", якщо значення зростають, "Decreasing" якщо спадають, інакше "Neither".
- **filter_true(boolean_list)**: Повертає список з істинних значень.
- **multiplexer(a, b, c, integer)**: Повертає `integer` помножене на 2 якщо `a` істинне, на 3 якщо `b` істинне, зменшене на 5 якщо `c` істинне, інакше повертає `integer`.

### Приклади використання
```python
# Перевірка істинності
print(check_truth(True, False, True))  # Output: True

# Логічна еквівалентність
print(logical_equivalence(True, True))  # Output: True

# XOR
print(xor(True, False))  # Output: True

# Привітання
print(greet(True))  # Output: Hello, World!
print(greet(False))  # Output: Goodbye, World!

# Вкладені умови
print(nested_condition(1, 1, 1))  # Output: All same
print(nested_condition(1, 2, 3))  # Output: All different

# Підрахунок істинних значень
print(count_true([True, False, True]))  # Output: 2

# Парність кількості одиниць
print(parity(5))  # Output: False

# Більшість голосів
print(majority_vote(True, False, True))  # Output: True

# Перемикання значення
print(switch(True))  # Output: False

# Тернарний оператор
print(ternary_check(True, "Yes", "No"))  # Output: Yes

# Перевірка комбінації
print(validate(True, False, True))  # Output: True

# Ланцюгова перевірка
print(chain_check(1, 2, 3))  # Output: Increasing
print(chain_check(3, 2, 1))  # Output: Decreasing

# Фільтрація істинних значень
print(filter_true([True, False, True]))  # Output: [True, True]

# Мультиплексор
print(multiplexer(True, False, False, 5))  # Output: 10
print(multiplexer(False, True, False, 5))  # Output: 15
print(multiplexer(False, False, True, 5))  # Output: 0
print(multiplexer(False, False, False, 5))  # Output: 5
```

## Результати
В процесі роботи були успішно реалізовані всі функції для роботи з логічними операціями. Тестування функцій підтвердило їх коректність та відповідність вимогам.

## Висновки
Мета роботи була досягнута. Було реалізовано та протестовано кілька функцій для вирішення задач, пов'язаних з логічними операціями та умовними виразами у Python. Всі завдання були виконані успішно, проблеми не виникли.

### Інструкції з запуску

Вимоги до середовища
- **Python версії 3.x

Команда для запуску
```
python main.py
```
