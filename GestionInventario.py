#color class that change the color of the text printed
class colors:
    """clase de colores tomada de: https://github.com/elcheryu-u/Riwi/blob/71d271813211caeefcf3403f005d46e7eea2c3cf/desarrollo/ruta-basica/M1/S3/ENTRENAMIENTO/gestion-inventario.py"""
    reset = '\033[0m'
    bold = '\033[01m'
    
    # colors
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'

#base structure for the principal Dictionary, and datas that are necesarie
inventory = {
    # "nombreProducto":("precio","cantidad")
}
answersAdding = ("si", "s", "no", "n")
answersMenu = (
    "1", "2", "3", "4", "5", "6", "7",
    "calcular", "consultar", "actualizar", "eliminar",
    "ingresar", "listar", "salir"
    )
validUpdate = False
validDelete = False
#######################TASK FUNCTIONS#########################

# The following two functions perform the same task: adding a new product to the inventory dictionary with its corresponding values.
# The difference is that one is a regular function, and the other is a lambda function.
def addProduct(dictionary, productName, productPrice, productQty):
    dictionary[productName] = (float(productPrice), int(productQty))
    return dictionary

addProductLambda = lambda dictionary, productName, productPrice, productQty:(dictionary.update({productName: (float(productPrice), int(productQty))}), dictionary)[1]

# Lambda and regular functions to search for a product by name in the dictionary
# and display a confirmation message based on whether it was found.
def consultByName(dictionary, productName):
    global validUpdate
    global validDelete
    if productName in dictionary.keys():
        print(f"Producto {colors.green}({productName}) encontrado!{colors.reset}")
        validUpdate = True
        validDelete = True        
        return dictionary[productName]
    else:
        validUpdate = False
        validDelete = False
        print(f"Producto {colors.red}({productName}) no encontrado!{colors.reset}")
        return False

consultByNameLambda = lambda dictionary, productName: ((print("Producto encontrado!"), dictionary[productName]) if productName in dictionary.keys() else print("Producto no encontrado!"))[1]

# Function to update the price of a product.
# REMINDER: Since the value in the dictionary is a tuple (price, quantity), it is immutable and cannot be modified directly.
# To update the price, a copy of the tuple must be made, preserving the quantity at position [1],
# while modifying the unit price at position [0]. The updated tuple is then reassigned to the dictionary.
def updateProductPrice(dictionary, productName, newPrice):
    try:
        temporaryArray = list(dictionary[productName])
        dictionary[productName] = (newPrice, temporaryArray[1])
        return dictionary
    except:
        print(f"{colors.red}ERROR: El producto no existe para modificar{colors.reset}")
        return

#delete product using product name and the metod del and for the lambda function i used the metod .pop to delete the key on the dictionary
#its becouse lambda functions only admite expresions but not instructions.
def deleteProductByName(dictionary, productName):
    try:
        del dictionary[productName]
        return dictionary
    except:
        print(f"{colors.red}ERROR: el producto no existe para eliminar{colors.reset}")    

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


def validationDictionary(dictionary):
    if dictionary != {}:
        return True
    else:
        return False
#function data values validation as numbers by decimal data type or integer data type and as a number that is bigger than 0.
def validationNumbers(data, type):
    try:
        if type == 1:
            float(data)
        elif type == 2:
            int(data)
        
        if float(data)>0:
            return True
        else:
            bonitificainador()
            print(f"{colors.red}ERROR: El valor ingresado debe ser mayor a (0). \nPor ende {data} no esta permitido.{colors.reset}")
            return False
    except ValueError:
        bonitificainador()
        if data.isalpha():
            print(f"{colors.red}ERROR: el valor ingresado no puede poseer alfanumericos. \nPor ende ({data}) no es admitido.{colors.reset}")
        if type == 2 and not(data.isalpha()):
            print(f"{colors.red}ERROR: el valor ingresado no puede ser decimal. \nPor ende ({data}) no es admitido.{colors.reset}")
        return False

#function for an input of price and calls the validation function.
def addPrice(inputProductPrice):
    while (validationNumbers(inputProductPrice,1)==False):
        inputProductPrice = input("Ingresa el precio unitario del producto: ")
    return inputProductPrice

#function for an input of price
def addQty(inputProductQty):
    while (validationNumbers(inputProductQty,2)==False):
        inputProductQty = input("Ingresa la cantidad del producto: ")
    return inputProductQty

#######################FUNCTIONS OF SEQUENCE#########################

#an function that ask if the user wants add a new product in a list here i need to use break to back to the OptionMenu
#couse he is in a while cicle that means if i call again the optionMenu the program will enter into a new while true cicle of optionMenu
def askingForNewProduct():
    while True:
        bonitificainador()
        answer = input("Desea ingresar un nuevo producto? (Si/No) \n")
        if (validateAnswer(answersAdding, answer) == True):
            if (answer.lower() == "si" or answer.lower() == "s"):
                return addMenu()
            else:
                break

#function charged to validate if an answer actually really exist in a list
def validateAnswer(answersList, answer):
    try:
        if answer in answersList:
            return True
        else:
            bonitificainador()
            print(f"{colors.red}ERROR: La respuesta ingresada ({answer}) no es valida!{colors.reset}")
            return False
    except:
        print("ERROR: en la validacion S/N.")

#logic function for the main Menu
def askingForOptionMainMenu():
    """Esta funcion valida primero que se ingrese una respuesta y segundo
      \nque dicha respuesta exista por medio de la funcion validadora de respuestas
      \npor ultimo compara cual fue la respuesta y dependiendo de la respuesta 
      \nllamara a un proceso u otro."""
    answer = input("\nQue deseas hacer? \n")
    if validateAnswer(answersMenu, answer):
        transformAnswertoSubprocess(answer)
        match answer.lower():
            case "1" | "calcular":
                calculationTotalMenu()
            case "2" | "consultar":
                consultMenu()
            case "3" | "actualizar":
                updatePriceMenu()
            case "4" | "eliminar":
                deleteProductMenu()
            case "5" | "ingresar":
                addMenu()
            case "6" | "listar":
                bonitificainador()
                print(colors.green, inventory, colors.reset)
                showMainMenu()
            case "7" | "salir":
                bonitificainador()
                print(" "*5,f"{colors.bold}{colors.lightblue}HASTA LUEGO!\n{colors.reset}")
                exit()
            case _:
                print("ERROR: Opcion no valida!")

#function charged to be the one who prints all the base Menu
def showMainMenu():
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
        askingForOptionMainMenu()

#this function restart the process called and if not close the actual process an back to the main proces and the while cicel in 
#OptionMenu
def restartProcess(actualProcess):
    bonitificainador()    
    while True:
        bonitificainador()
        answer = input("Desea intentar de nuevo el proceso? (Si/No) \n")
        if (validateAnswer(answersAdding, answer)):
            if (answer.lower() == "si" or answer.lower() == "s"):               
                return actualProcess()                
            else:
                return None

def bonitificainador():
    """The best function ever."""
    print(f"{colors.blue}==" * 40, "\n",colors.reset)

def transformAnswertoSubprocess(answer):
    global subProcess
    match answer.lower():
            case "1" | "calcular":
                answer = 1
            case "2" | "consultar":
                answer = 2
            case "3" | "actualizar":
                answer = 3
            case "4" | "eliminar":
                answer = 4
    subProcess = answer
        
####################INPUT OR MENU-AREA##############################
def addMenu():
    bonitificainador()
    print("--"*5,f"{colors.bold}{colors.blue}INGRESO DE INVENTARIO{colors.reset}","--"*5)
    productName = input(f"{colors.yellow}1{colors.reset} - Ingresa el nombre del producto{colors.purple}:{colors.reset} \n     ")

    #peticion y funcion de 
    productPrice = input(f"{colors.yellow}2{colors.reset} - Ingresa el precio unitario del producto{colors.purple}:{colors.reset} \n     ")
    productPrice = addPrice(productPrice)

    productQty = input(f"{colors.yellow}3{colors.reset} - Ingresa la cantidad del producto{colors.purple}:{colors.reset} \n     ")
    productQty = addQty(productQty)

    #Lambda implementation of the valid values
    addProductLambda(inventory, productName, productPrice, productQty)
    print(f"{colors.green}Producto ingresado correctamente: {productName}\nPrecio: {productPrice}$\nCantidad: {productQty}{colors.reset}")
    return askingForNewProduct()

def consultMenu():
    bonitificainador()
    if subProcess==2:
        print("--"*5,f"{colors.bold}{colors.blue}CONSULTA DE INVENTARIO{colors.reset}","--"*5)
        prompt = (f"{colors.yellow}+{colors.reset} - Ingresa el nombre del producto que desea consultar: {colors.purple}:{colors.reset} \n     ")
    elif subProcess == 3:
        print("Entrada de actualizar")
        prompt = (f"{colors.yellow}+{colors.reset} - Ingresa el nombre del producto que desea modificar: {colors.purple}:{colors.reset} \n     ")
    elif subProcess == 4:
        print("Entrada de eliminar")
        prompt = (f"{colors.yellow}+{colors.reset} - Ingresa el nombre del producto que desea eliminar: {colors.purple}:{colors.reset} \n     ")

    if(validationDictionary(inventory)==True):
        consultName = input(prompt)
        
        consultedProduct = consultByName(inventory,consultName)        
        try:            
            if consultedProduct:
                print(f"{colors.bold}{colors.green}Precio unitario: {float(consultedProduct[0])}. \nCantidad: {int(consultedProduct[1])}{colors.green}")
                if (subProcess == 3 or subProcess == 4):                                      
                    return consultName
                return restartProcess(consultMenu)
            else:
                if subProcess in (3,4):                  
                    return restartProcess(deleteProductMenu if subProcess == 4 else updatePriceMenu)
                return restartProcess(consultMenu)
        except:
            print("ERROR: En restartProcess o su llamada!")
    else:
        print(f"{colors.red}ERROR: No has agregado ningun producto a tu inventario.{colors.reset}")
        return askingForNewProduct()

def updatePriceMenu():    
    bonitificainador()
    print("--"*5,f"{colors.bold}{colors.blue}MODIFICACION DE INVENTARIO{colors.reset}","--"*5)
    consultedproductName =  consultMenu()    
    if (validUpdate):
        newProductPrice = input(f"{colors.yellow}+{colors.reset} - Ingresa el nuevo precio unitario del producto{colors.purple}:{colors.reset} \n     ")        
        newProductPrice = addPrice(newProductPrice)
        updateProductPrice(inventory,consultedproductName,newProductPrice)
        bonitificainador()
        print("--"*5,f"{colors.bold}{colors.green}PRODUCTO MODIFICADO EXITOSAMENTE{colors.reset}","--"*5)
        print(f"{colors.bold}{colors.green}Producto: {consultedproductName}\nNuevo precio unitario: {float(inventory[consultedproductName][0])}.{colors.reset}")
        return restartProcess(updatePriceMenu)
    else:
        if (validationDictionary(inventory)):
            print(f"{colors.red}ERROR: No se puede modificar un producto que no existe.{colors.reset}")        

def deleteProductMenu():
    bonitificainador()
    print("--"*5,f"{colors.bold}{colors.blue}ELIMINACION DE INVENTARIO{colors.reset}","--"*5)
    consultedproductName =  consultMenu()

    if consultedproductName == None:
        return

    if (validDelete):               
        deleteProductByName(inventory,consultedproductName)
        bonitificainador()
        print(f"{colors.green}Producto '{consultedproductName}' eliminado exitosamente.{colors.reset}")
        return restartProcess(deleteProductMenu)
    else:        
        if (validationDictionary(inventory)):
            print(f"{colors.red}ERROR: No se puede eliminar un producto que no existe.{colors.reset}")

def calculationTotalMenu():
    if validationDictionary(inventory):
        bonitificainador()
        print("--"*5,f"{colors.bold}{colors.blue}SUMATORIA DEL COSTO TOTAL DEL INVENTARIO{colors.reset}","--"*5)
        multipliedPricesList = calculateProductCostValues(inventory)
        totalPrices = sumTotalPricesLambda(multipliedPricesList)
        print(f"{colors.bold}{colors.blue}El valor de compra de todos los PRODUCTOS:{colors.reset}\n{colors.lightblue}{inventory} \nEs de: {colors.reset}{colors.yellow}{colors.bold}{totalPrices}${colors.reset}")
        restartProcess(calculationTotalMenu)
    else:
        print(f"{colors.red}ERROR: no se puede calcular ningun total si no hay ningun producto.{colors.reset}")

showMainMenu()