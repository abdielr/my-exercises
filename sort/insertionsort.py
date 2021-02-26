lista = [4,2,6,8,5,7]
print(lista)
print()
for i in range(1,len(lista)):
    aux = lista[i]
    j = i - 1
    while j >= 0 and aux < lista[j]:
        lista[j+1] = lista[j]
        lista[j] = aux
        j -= 1
print(lista)