def esta_atacando(row1, col1, row2, col2):
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def lugar_reynas(n, row, reynas):
    if n == row:
        print(reynas)
        return True

    for col in range(n):
        no_atacando = True
        for reyna in reynas[:row]:
            if esta_atacando(reyna[0], reyna[1], row, col):
                no_atacando = False
                break

        if no_atacando:
            reynas.append((row, col))
            if lugar_reynas(n, row + 1, reynas):
                return True
            reynas.pop()

    return False

def resolver_n_reynas(n):
    if n <= 0:
        print("No hay solución para {} reynas.".format(n))
        return

    reynas = []
    if lugar_reynas(n, 0, reynas):
        print("Encontré una solución para {} reinas:".format(n))
        print(reynas)
    else:
        print("No hay solución para {} reinas.".format(n))      

resolver_n_reynas(8)
