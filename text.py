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

def count_x(s):
    if not s:
        return 0
    if s[0] == 'x':
        return 1 + count_x(s[1:])
    else:
        return count_x(s[1:])
text = "example text"
result = count_x(text)
print(f"'x' зустрічається {result} разів у рядку.")

