lista = [12,5,78,2,4,8,1,0,3,77,64,90]

def sort(lista):
    for i in range(1,len(lista)):
        aux = lista[i]
        j = i - 1
        while j >= 0 and aux < lista[j]:
            lista[j+1] = lista[j]
            lista[j] = aux
            j -= 1
    return lista

def busquedaBinaria(dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <=derecha:
        medio = (izquierda + derecha)//2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio -1
        else: 
            izquierda = medio + 1
    return None
def buscar(dato):
    sort(lista)
    if busquedaBinaria(dato) == None:
        return "El dato %d no se encontro"%(dato)
    else:
        return "El dato %d se encontro en el indice: %d"%(dato,busquedaBinaria(dato))


print (buscar(90))