result = []
def divider(a, b):
    if a < b:
        raise ValueError("ValueError: перше число менше за друге.")
    if b > 100:
        raise IndexError("IndexError: друге число більше за 100.")
    if b == 0:
        raise ZeroDivisionError("ZeroDivisonError: ділення на нуль.")
    return a / b

data = {10: 2, 2: 5, 123: 4, 18: 0, 19: 15, 8 : 4}
print(data)
try:
    for key in data:
        print("Перше число:", key)
        print("Друге число:", data[key])
        res = divider(key, data[key])
        print("Результат:", res, "\n")
        result.append(res)
except (ValueError, IndexError, ZeroDivisionError) as error:
    print("Error", error)
print(result)