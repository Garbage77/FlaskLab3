from comb_sort import comb_sort
from data_loader import random_arr

def test_shell_sort(test_size):
   
   # Создаем случайный массив указанной длины
    arr = random_arr(int(test_size))
    reverse = False  # Сортировка по возрастанию
    comb_sort(arr)
   # Выводим отсортированный  
