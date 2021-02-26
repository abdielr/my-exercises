lista = [12,5,78,2,4,8,1,0,3,77,64,90]

def busquedaLineal(dato):
    for x in range(len(lista)):
        if lista[x] == dato:
            return x
    return None

def buscar(dato):
    if busquedaLineal(dato) == None:
        return"Item not found"
    else:
        return ("Se encontro el dato "+ str(dato))



print(lista)
print(buscar(11111))