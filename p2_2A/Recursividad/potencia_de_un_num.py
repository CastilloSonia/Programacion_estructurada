def power(base, exponent):
    if exponent == 0:  # Caso base
        return 1
    else:
        return base * power(base, exponent - 1)  # Caso recursivo.
print(power(2, 3))