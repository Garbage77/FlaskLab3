# Функция сортировки Расчёской
def comb_sort(arr):
    
    jump = len(arr)
    fact = 1.25
    swapped = True
    
    while jump >= 1 or swapped:
        swapped = False
        
        for i in range (len(arr) - jump):
            if arr[i] > arr[i+jump]:
                arr[i], arr[i+jump] = arr[i+jump], arr[i]
                swapped = True
                
        jump = (int)(jump / fact);

    return arr
