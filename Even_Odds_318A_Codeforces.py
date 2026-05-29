n, k = map(int, input() . split())
qtd_impares = (n + 1) // 2
if k <= qtd_impares:
    print(2 * k - 1)
else:
    print((k - qtd_impares) * 2)