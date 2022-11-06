import random
import math
def menu():
    ch = -1
    while (ch<0) or (ch>7):
        print('\n1. Создать случайный набор данных в массиве\n'
              '2. Отобразить массив\n'
              '3. Сортировка вставками\n'
              '4. Cортировка выбором\n'
              '5. Пузырьковая сортировка\n'
              '6. Сортировка слиянием\n'
              '7. Сортировка Шелла\n'
              '8. Быстрая сортировка\n'
              '0. Выход\n')
        ch = int(input('Выберите пункт из меню: '))
        return ch

def create_arr():
    size = int(input('Введите размер массива: '))
    arr = [0] * size
    for i in range(size):
        arr[i] = int(round(random.random() * 100, 0))
    return arr

def showing(arr):
    print('Ваш массив:', arr)

def sort_vstav(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = a
    print ('Отсортированный массив:', arr)

def sort_vibor(arr):
    for i in range(0, len(arr) - 1):
        small = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    print('Отсортированный массив:', arr)

def sort_pyz(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print('Отсортированный массив:', arr)


def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

def sort_slyan(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    print('Отсортированный массив:', arr)


def sort_shell(arr):
    n = len(arr)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        k -= 1
        interval = 2 ** k - 1
    print('Отсортированный массив:', arr)


def sort_fast(arr):
    if len(arr) > 1:
        c = arr.pop()
        grtr_lst, equal_lst, smlr_lst = [], [c], []
        for item in arr:
            if item == c:
                equal_lst.append(item)
            elif item > c:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
    arr.append(equal_lst[0])
    print('Отсортированный массив:', arr)

def main():
    ch=-1
    while (ch!=0):
        ch = menu()

        if ch == 1:
            arr = create_arr()

        elif ch == 2:
            showing(arr)

        if ch == 3:
            sort_vstav(arr)

        if ch == 4:
            sort_vibor(arr)

        if ch == 5:
            sort_pyz(arr)

        if ch == 6:
            sort_slyan(arr)

        if ch == 7:
            sort_shell(arr)

        if ch == 8:
            sort_fast(arr)


main()