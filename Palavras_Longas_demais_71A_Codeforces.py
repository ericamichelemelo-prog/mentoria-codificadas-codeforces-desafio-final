n = int(input())
for i in range(n):
    palavra = input()
    tamanho = len(palavra)
    if tamanho > 10:
        print(palavra[0] + str(tamanho - 2) + palavra [-1])
    else:
        print(palavra)