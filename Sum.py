lista = [[1, 5, 3], [12, 18], [21, 36, 48]]
soma_total = sum(sum(sublista) for sublista in lista)
print("A soma dos elementos é: {}".format(soma_total))