def faktoriyel(n):
    if n==0:
        return 1
    else:
        return n * faktoriyel(n-1)

print(faktoriyel(4))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

def binary_Search_recursive(arr , low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_Search_recursive(arr, low,  mid - 1, target)
    else:
        return binary_Search_recursive(arr, mid + 1, high, target)
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

result = binary_Search_recursive(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"{target} elemanı {result}. indexte bulundu.")
else:
    print(f"{target} elemanı bulunamadı.")

def selection_sort_recursive(arr, n):
    if n == 1:
        return

    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i

    arr[n-1], arr[max_idx] = arr[max_idx], arr[n-1]
    selection_sort_recursive(arr, n-1)

arr = [64, 25, 12, 22, 11, 3, 23, 0, 12]
n = len(arr)
print("Sıralanmamış dizi: ",arr)
selection_sort_recursive(arr, n)
print("Sıralanmış dizi: ",arr)