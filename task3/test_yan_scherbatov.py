"""
Задача №3:
У нас есть функция, которая выводит данные студентов.
Наша задача - написать класс-декоратор,
который выводит имена студентов старше заданного возраста.

Например:
>>> @AgeCalculator(40)
... def my_func(student: Student):
...     print(f'Студент: {student.name}, возраст: {student.age}')
>>> my_func(Student(name='Анфиса Питоновна', age=23))
Студент: Анфиса Питоновна, возраст: 23

>>> my_func(Student(name='Григорий Распутин', age=47))
Возраст студента Григорий Распутин > 40
Студент: Григорий Распутин, возраст: 47

>>> my_func(Student(name='Драко Малфой', age=12))
Студент: Драко Малфой, возраст: 12

>>> my_func(Student(name='Пётр I', age=52))
Возраст студента Пётр I > 40
Студент: Пётр I, возраст: 52
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    age: int

# Ваш код должен быть тут :)
# Не меняйте остальные строчки!
# Чтобы проверить, правильно ли вы сделали задание,
# Просто запустите файл в VSCode или выполните
# `python <имя_вашего_файла> -V` в консоли
def my_func(student: Student):
    print(f'Студент: {student.name}, возраст: {student.age}')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
