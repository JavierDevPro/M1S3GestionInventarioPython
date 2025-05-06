#Estructura base del producto
inventory = {
    # "nombreProducto":("precio","cantidad")
}
answersAdding = ("si", "s", "no", "n")
answersMenu = ("1","2","3","4","5","calcular", "consultar", "actualizar", "eliminar", "ingresar")

#######################TASK FUNCTIONS#########################

#las siguientes dos funciones realizan la misma funcion que es agregar al diccionario product un nuevo producto con sus valores respectivos
#la diferencia es que una es normal y la otra es lambda
def add(dictionary, productName, productPrice, productQty):
    dictionary[productName] = (productPrice, productQty)
    return dictionary

addProductLambda = lambda dictionary, productName, productPrice, productQty:(dictionary.update({productName: (productPrice, productQty)}), dictionary)[1]

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

#delete product using product name and the metod del and for the lambda function i used the metod .pop to delete the key on the dictionary
#its becouse lambda functions only admite expresions but not instructions.
def deleteProductByName(dictionary, productName):
    del dictionary[productName]
    return dictionary

deleteProductByNameLambda = lambda dictionary, productName: dictionary.pop(productName)

#fuction that obtein one list with the product value from multiply the values of every single product ("price","productQty")
def calculateProductCostValues(dictionary):
    multipliedPricesList = []
    for sublist in dictionary.values():
        multipliedPricesList.append(float(sublist[0]) * int(sublist[1]))
    return multipliedPricesList

#fuction and lambda function sum values from a prices list calculated list
def sumTotalPrices(pricesList):
    totalPricesProducts = sum(pricesList)
    return totalPricesProducts

sumTotalPricesLambda = lambda pricesList: sum(pricesList)

#######################FUNCTIONS OF VALIDATIONS AND INPUTS#########################

#function data values validation as numbers and as a number that is bigger than 0.
def validationNumbers(data):
    try:
        float(data)
        if float(data)>0:
            return True
        else:
            bonitificainador()
            print(f"ERROR: El valor ingresado debe ser mayor a (0). \nPor ende {data} no esta permitido.")
            return False
    except ValueError:
        bonitificainador()
        print(f"ERROR: el valor ingresado no puede poseer alfanumericos. \nPor ende ({data}) no es admitido.")
        return False

#function for an input of price
def addPrice(inputProductPrice):    
    while (validationNumbers(inputProductPrice)==False):
        inputProductPrice = input("Ingresa el precio unitario del producto: ")    
    return inputProductPrice

#function for an input of price
def addQty(inputProductQty):
    while (validationNumbers(inputProductQty)==False):
        inputProductQty = input("Ingresa la cantidad del producto: ")    
    return inputProductQty

#######################FUNCTIONS OF SEQUENCE#########################

#an function that ask if the user wants add a new product in a list
def askingForNewProduct():
    while True:
        bonitificainador()
        answer = input("Desea ingresar un nuevo producto? (Si/No) \n")
        if (validateAnswer(answersAdding, answer) == True):
            if (answer.lower() == "si" or answer.lower() == "s"):
                return main()
            else:
                return optionMenu()

#function charged to validate if an answer actually really exist in a list
def validateAnswer(answersList, answer):
    if answer in answersList:
        return True
    else:
        bonitificainador()
        print(f"ERROR: La respuesta ingresada {answer} no es valida!")
        return False
    
def optionMenu():
    while True:
        bonitificainador()
        print("                 Menu opciones                      \n")
        print("(1) - calcular total de la compra.\n")
        print("(2) - consultar un valores de un producto.\n")
        print("(3) - actualizar precios del producto.\n")
        print("(4) - eliminar producto.\n")
        print("(5) - ingresar mas productos.\n")
        answer = input("\nQue deseas hacer? \n")
        if (validateAnswer(answersMenu, answer)==True):
            match answer.lower():
                case "1" | "calcular":
                    break
                case "2" | "consultar":
                    break
                case "3" | "actualizar":
                    break
                case "4" | "eliminar":
                    break
                case _:
                    main()

def bonitificainador():
    print("##" * 50, "\n")
        
#####################Secuense-test#############################
# consulta = input("Consulta por nombre al producto: ")
# consultedValues = consultByNameLambda(inventario, consulta)
# print(consultedValues)
# print(inventario)

# newProductPrice = input("Ingrese el nuevo valor para el producto: ")
# updateProductPrice(inventario, consulta, newProductPrice)
# print(inventario)

# eliminar = input("Ingrese un producto del inventario para eliminar: ")
# deleteProductByNameLambda(inventario, eliminar)
# print(inventario)

# multipliedPricesList = calculateProductCostValues(inventario)
# print(multipliedPricesList)
# totalPrices = sumTotalPricesLambda(multipliedPricesList)
# print(totalPrices)

####################input-test##############################
def main():
    bonitificainador()
    productName = input("Ingresa el nombre del producto: \n")

    #peticion y funcion de 
    productPrice = input("Ingresa el precio unitario del producto: \n")
    productPrice = addPrice(productPrice)

    #
    productQty = input("Ingresa la cantidad del producto: \n")
    productQty = addQty(productQty)

    #
    addProductLambda(inventory, productName, productPrice, productQty)
    print(inventory)

    askingForNewProduct()

main()