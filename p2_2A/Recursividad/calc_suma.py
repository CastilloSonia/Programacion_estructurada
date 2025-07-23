def sum_recursive(num):
    if num == 1:  # Caso base
        return num
    return num + sum_recursive(num - 1)  # Caso recursivo.

print(sum_recursive(3)) # 3 + 2 + 1 