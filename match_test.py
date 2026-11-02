"""
    Блок тестов для Match, 
    имя любой функции должно быть со словом ( test )
"""

import inspect
from typing import Any, Dict, Optional

# Конструкция выглядит несколько опасно. Многозначно.
# Не смог вызвать help на match. Чет на него ничего нет.
# судя по тестам там можно условий наворотить, всё что возвращает bool
# !!! guards решает

def test_match_1_default() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    flag = False
    match (100, 200):
        case (100, 300):  # Mismatch: 200 != 300
            print('Case 1')
        case (100, 200) if flag:  # Successful match, but guard fails
            print('Case 2')
        case (100, y):  # Matches and binds y to 200
            print(f'Case 3, y: {y}')
        case _:  # Pattern not attempted
            print('Case 4, I match anything!')

def test_match_2() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    flag = True
    match (100, 200):
        case (100, 300):  # Mismatch: 200 != 300
            print('Case 1')
        case (100, 200) if flag:  # Successful match, but guard fails
            print('Case 2')
        case (100, y) if flag:  # Matches and binds y to 200
            print(f'Case 3, y: {y}')
        case _:  # Pattern not attempted
            print('Case 4, I match anything!')

def test_match_3() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    flag = False
    match (100, 200):
        case (100, 300):
            print('Case 1')
        case (100, 200) if flag:
            print('Case 2')
        case (100, y) if flag:
            print(f'Case 3, y: {y}')
        case _:  # # Successful match
            print('Case 4, I match anything!')

def test_match_4() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    match (100, 200):
        case (100, 300):
            print('Case 1')
        case (100, 200) if (True if 1 > 3 else False):  
            print('Case 2')
        case (100, y) if (True if 1 < 3 else False):  # Successful match
            print(f'Case 3, y: {y}')
        case _:
            print('Case 4, I match anything!')

def test_match_5() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    match (100, 200):
        case (100, 300):  
            print('Case 1')
        case (100, 200) if all([1,1,1]):  # Successful match
            print('Case 2')
        case (100, y) if (True if 1 < 3 else False): 
            print(f'Case 3, y: {y}')
        case _:  
            print('Case 4, I match anything!')

def test_match_6() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    match (100, 200):
        case (100, 300):
            print('Case 1')
        case (100, 200) if lambda x: True :  # Successful match
            print('Case 2')
        case (100, y) if (True if 1 < 3 else False):  
            print(f'Case 3, y: {y}')
        case _:  
            print('Case 4, I match anything!')

def test_match_7() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    match (100, 200):
        case (100, 300):
            print('Case 1')
        case (100, 200) if not [] :  # Successful match
            print('Case 2')
        case (100, y) if (True if 1 < 3 else False):  
            print(f'Case 3, y: {y}')
        case _:  
            print('Case 4, I match anything!')

def test_match_8() -> Any:
    func_name = inspect.stack()[0].function
    print(f"Функция: {func_name}")
    match (100, 200):
        case (100, 300):
            print('Case 1')
        case (100, 200) if not [] :  # Successful match
            print('Case 2')
        case (100, y) if (True if 1 < 3 else False):  
            print(f'Case 3, y: {y}')
        case _:  
            print('Case 4, I match anything!')

def f_launcher(g: Optional[Dict[str, Any]] = None, /) -> None:
    """
    Запускает функции в именах которых есть слово test.  

    Args:
        g (dict, optional): По умолчанию параметр None, заменяется на globals().
        где key имена функций, а val вызываемые объекты

    Exceptions:
        Если аргумент "g" не является словарём

    Returns:
        None
    """
    if g is None:
        g = globals()

    if not isinstance(g, dict):
        raise ValueError('Переменная "g" не соответствует типу dict')
    
    for func_name, func_object in g.items():
            if 'test' in func_name and callable(func_object):
                func_object()

f_launcher()

# Тут у нас есть охранник, текст ниже, нужно еще раз осмыслить
# https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
# 8.6.2. Guards¶
# guard: "if" assignment_expression
# A guard (which is part of the case) must succeed for code inside the case block to execute. It takes the form: if followed by an expression.
# The logical flow of a case block with a guard follows:
# Check that the pattern in the case block succeeded. If the pattern failed, the guard is not evaluated and the next case block is checked.
# If the pattern succeeded, evaluate the guard.
# If the guard condition evaluates as true, the case block is selected.
# If the guard condition evaluates as false, the case block is not selected.
# If the guard raises an exception during evaluation, the exception bubbles up.
# Guards are allowed to have side effects as they are expressions. Guard evaluation must proceed from the first to the last case block,
# one at a time, skipping case blocks whose pattern(s) don’t all succeed. 
# (I.e., guard evaluation must happen in order.) Guard evaluation must stop once a case block is selected.

# guard: "if" assignment_expression
# Guard (который является частью case) должен успешно выполниться, чтобы код внутри блока case исполнился. Он имеет форму: if, за которым следует выражение.
# Логика выполнения блока case с guard следующая:
# Проверяется, что шаблон в блоке case совпал. Если шаблон не совпал, guard не вычисляется и проверяется следующий блок case.
# Если шаблон совпал, вычисляется guard.
# !!! Если условие guard истинно, блок case выбирается. ( ПРОВЕРИТЬ/проверено )
# Если условие guard ложно, блок case не выбирается.
# Если при вычислении guard возникает исключение, оно распространяется вверх. 
#   ( Наверно имеется ввиду что ошибка если появится, то не покажет на блок кейс, а укажет на то место где условие прописано )
# Guard'ам разрешено иметь побочные эффекты, так как они являются выражениями. Вычисление guard'ов должно происходить от первого к последнему блоку case,
# по одному за раз, пропуская блоки case, чьи шаблон(ы) не все совпали.
#   Не очень понимаю что имеется ввиду, но мне кажется что вот этот флаг защиты лучше прописывать не впроцессе, а до процесса сравнения.
#   Чтобы не усложнять чтение кода
# (То есть вычисление guard'ов должно происходить по порядку.) Вычисление guard'ов должно прекратиться, как только блок case выбран.