#Estructura base del inventario
inventario = {
    "nombreProducto":("precio","cantidad")
}

#las siguientes dos funciones realizan la misma funcion que es agregar al diccionario inventario un nuevo producto con sus valores respectivos
#la diferencia es que una es normal y la otra es lambda
def add(dictionary, productName, productPrice, productQty):
    dictionary[productName] = (productPrice, productQty)
    return dictionary

addLambda = lambda dictionary, productName, productPrice, productQty:(dictionary.update({productName: (productPrice, productQty)}), dictionary)[1]

#funciones lambda y no lambda de consultar en el diccionario segun el nombre del producto e imprimir mensaje de confirmacion
def consultByName(dictionary, productName):
    if productName in dictionary.keys():
        print("Producto encontrado!")
        return dictionary[productName]
    else:
        print("Producto no encontrado!")

consultByNameLambda = lambda dictionary, productName: ((print("Producto encontrado!"), dictionary[productName]) if productName in dictionary.keys() else print("Producto no encontrado!"))[1]

#funcion que actualice el precio, RECORDATORIO: como el valor en el diccionario es una tupla el valor no se puede modificar directamente es por ello que 
#se tiene que modificar indirectamente tomando una copia de la tupla para poder acceder a las posiciones exacta de los valores y luego asi mantener el valor
#de la posicion 1 que representa la cantidad de productos y poder modificar el precio unitario en la posicion[0]
def updateProductPrice(dictionary, productName, newPrice):
    temporaryArray = list(dictionary[productName])
    dictionary[productName] = (newPrice, temporaryArray[1])
    return dictionary

#delete product


#####################test#############################
productName = input("Ingresa el nombre del producto: ")
productPrice = input("Ingresa el precio unitario del producto: ")
productQty = input("Ingresa la cantidad del producto: ")
addLambda(inventario, productName, productPrice, productQty)
print(inventario)

consulta = input("Consulta por nombre al producto: ")
consultedValues = consultByNameLambda(inventario, consulta)
print(consultedValues)
print(inventario)

newProductPrice = input("Ingrese el nuevo valor para el producto: ")
updateProductPrice(inventario, consulta, newProductPrice)
print(inventario)