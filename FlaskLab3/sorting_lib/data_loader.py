# -*- coding: utf-8 -*-
import random

# Функция для загрузки данных
def random_arr(size, min=0, max=10000):
    """Генерирует массив случайных чисел.
    
    Args:
        size (int): Размер массива.
        min (int): Минимальное значение. По умолчанию 0.
        max (int): Максимальное значение. По умолчанию 100.
    
    Returns:
        list: Список случайных чисел.
    """
    return [random.randint(min, max) for _ in range(size)]
