def compute_factorial(num):
    if num == 0:  # Caso base
        return 1
    return num * compute_factorial(num - 1)  # Caso recursivo

print(compute_factorial(4)) # 4 * 3 * 2 * 1
