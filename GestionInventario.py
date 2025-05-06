class colors:
    """clase de colores"""
    reset = '\033[0m'
    bold = '\033[01m'
    
    # colores
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'

#Estructura base del producto
inventory = {
    # "nombreProducto":("precio","cantidad")
}
answersAdding = ("si", "s", "no", "n")
answersMenu = ("1","2","3","4","5","calcular", "consultar", "actualizar", "eliminar", "ingresar", "6", "listar", "7", "salir")

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
        print(f"Producto {colors.green}({productName}) encontrado!{colors.reset}")
        return dictionary[productName]
    else:
        print(f"Producto {colors.red}({productName}) no encontrado!{colors.reset}")

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
def validationDictionary(dictionary):
    if dictionary != {}:
        return True
    else:
        return False
    
def validationNumbers(data):
    try:
        float(data)
        if float(data)>0:
            return True
        else:
            bonitificainador()
            print(f"{colors.red}ERROR: El valor ingresado debe ser mayor a (0). \nPor ende {data} no esta permitido.{colors.reset}")
            return False
    except ValueError:
        bonitificainador()
        print(f"{colors.red}ERROR: el valor ingresado no puede poseer alfanumericos. \nPor ende ({data}) no es admitido.{colors.reset}")
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
                return addMenu()
            else:
                return showOptionMenu()

#function charged to validate if an answer actually really exist in a list
def validateAnswer(answersList, answer):
    if answer in answersList:
        return True
    else:
        bonitificainador()
        print(f"{colors.red}ERROR: La respuesta ingresada ({answer}) no es valida!{colors.reset}")
        return False
    
def askingForOptionMenu():
    """Esta funcion valida primero que se ingrese una respuesta y segundo
      \nque dicha respuesta exista por medio de la funcion validadora de respuestas
      \npor ultimo compara cual fue la respuesta y dependiendo de la respuesta 
      \nllamara a un proceso u otro."""
    answer = input("\nQue deseas hacer? \n")
    if (validateAnswer(answersMenu, answer)==True):
        match answer.lower():
            case "1" | "calcular":
                exit()
            case "2" | "consultar":
                consultMenu()
            case "3" | "actualizar":
                ()
            case "4" | "eliminar":
                ()
            case "5" | "ingresar":
                addMenu()
            case "6" | "listar":
                print(colors.green, inventory, colors.reset)
                showOptionMenu()
            case "7" | "salir":
                bonitificainador()
                print(" "*5,f"{colors.bold}{colors.lightblue}HASTA LUEGO!\n{colors.reset}")
                exit()
            case _:
                print("ERROR: Opcion no valida!")


def showOptionMenu():    
    """
    Muestra el menu de opciones principal del
    """
    while True:
        bonitificainador()
        print("--"*5,f"{colors.bold}{colors.blue}MENU DE OPCIONES{colors.reset}","--"*5)
        print(f"{colors.yellow}(1){colors.reset} - calcular total de la compra.")
        print(f"{colors.yellow}(2){colors.reset} - consultar valores de un producto.")
        print(f"{colors.yellow}(3){colors.reset} - actualizar precios del producto.")
        print(f"{colors.yellow}(4){colors.reset} - eliminar producto.")
        print(f"{colors.yellow}(5){colors.reset} - ingresar productos.")
        print(f"{colors.yellow}(6){colors.reset} - listar productos.")
        print(f"{colors.yellow}(7){colors.reset} - salir.")
        askingForOptionMenu()

def retryProcess(actualProcess):
    bonitificainador()
    while True:
        bonitificainador()
        answer = input("Desea intentar de nuevo el proceso? (Si/No) \n")
        if (validateAnswer(answersAdding, answer) == True):
            if (answer.lower() == "si" or answer.lower() == "s"):
                return actualProcess()
            else:
                return showOptionMenu()

def bonitificainador():
    print(f"{colors.blue}==" * 40, "\n",colors.reset)
        
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
def addMenu():
    bonitificainador()
    print("--"*5,f"{colors.bold}{colors.blue}INGRESO DE INVENTARIO{colors.reset}","--"*5)
    productName = input(f"{colors.yellow}1{colors.reset} - Ingresa el nombre del producto{colors.purple}:{colors.reset} \n     ")

    #peticion y funcion de 
    productPrice = input(f"{colors.yellow}2{colors.reset} - Ingresa el precio unitario del producto{colors.purple}:{colors.reset} \n     ")
    productPrice = addPrice(productPrice)

    #
    productQty = input(f"{colors.yellow}3{colors.reset} - Ingresa la cantidad del producto{colors.purple}:{colors.reset} \n     ")
    productQty = addQty(productQty)

    #
    addProductLambda(inventory, productName, productPrice, productQty)
    print(inventory)
    askingForNewProduct()

def consultMenu():
    bonitificainador()
    print("--"*5,f"{colors.bold}{colors.blue}CONSULTA DE INVENTARIO{colors.reset}","--"*5)
    if(validationDictionary(inventory)==True):
        consultName = input("Consulta por nombre al producto: ")
        consultedProduct = consultByName(inventory,consultName)
        print(f"{colors.bold}{colors.green}Precio unitario: {float(consultedProduct[0])}. \nCantidad: {int(consultedProduct[1])}{colors.green}")
        retryProcess(consultMenu)    
    else:
        print(f"{colors.red}ERROR: No has agregado ningun producto a tu inventario.{colors.reset}")
        askingForNewProduct()



def main():
    showOptionMenu()

main()