# Функция для сохранения массива в файл
def saver(arr, file="output.txt"): 
    """Сохраняет массив в текстовый файл.
    
    Args:
        arr (list): Массив для сохранения.
        file (str): Имя файла для сохранения. По умолчанию 'output.txt'.
    """
    with open(file, "w") as f:
        for value in arr:
            f.write(f"{value}\n")
