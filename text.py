# def num(n):
#     if n == 0:
#         return 0 
#     else:
#         return n  + num(n - 1)

# n = 5
# print(f"Sum number for 1 to {n}: {num(n)}")

# Task2


# def row(t):
#     if len(t) == 0:
#         return ""
#     else:
#         return row(t[1:]) + t[0]

# text = "My dream is to visit New York"

# print(f"Звичайний рядок: {text}")
# print(f"Рядок в зворотньому порядку: {row(text)}")

# def count_x(s):
#     if not s:
#         return 0
#     if s[0] == 'x':
#         return 1 + count_x(s[1:])
#     else:
#         return count_x(s[1:])
# text = "example text"
# result = count_x(text)
# print(f"'x' зустрічається {result} разів у рядку.")


# def search(arr, target):
#     if not arr:
#         return -1
    
#     mid = len(arr) // 2
    
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         result = search(arr[mid + 1:], target)
#         return mid + 1 + result if result != -1 else -1
#     else:
#         return search(arr[:mid], target)
    
# sorted_list = [1, 3, 7, 5, 9, 11, 13, 15, 17, 19]
# target_value = 5

# result = search(sorted_list, target_value)

# if result != -1:
#     print(f"Значення {target_value} знайдено на індексі {result}.")
# else:
#     print(f"Значення {target_value} не знайдено у списку.")

