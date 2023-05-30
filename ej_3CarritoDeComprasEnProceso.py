
productos = {
    "producto1": {
        "codigo_producto": "001",
        "nombre_producto": "Camiseta",
        "marca_producto": "Nike",
        "precio_producto": 29.99,
        "stock_producto": 50,
        "color_producto": "Negro",
        "caracteristicas_producto": "Algodón 100%, talla M"
    },
    "producto2": {
        "codigo_producto": "002",
        "nombre_producto": "Pantalón",
        "marca_producto": "Adidas",
        "precio_producto": 49.99,
        "stock_producto": 30,
        "color_producto": "Azul",
        "caracteristicas_producto": "Poliéster, talla L"
    },
    "producto3": {
        "codigo_producto": "003",
        "nombre_producto": "Zapatos",
        "marca_producto": "Puma",
        "precio_producto": 69.99,
        "stock_producto": 20,
        "color_producto": "Blanco",
        "caracteristicas_producto": "Cuero genuino, talla 42"
    }
}

def codigo():
    codigo_producto= input("Ingrese el codigo numerico del producto... " )
    opcion=input(f"El codigo ingresado es {codigo_producto}, si desea modificarlo presione ( n ), de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar el codigo del producto...")       
        return codigo()
    else:
        if codigo_producto.isdigit():
            return codigo_producto
        else:
            print("Ingrese el codigo del producto en numeros, vuleva a ingresar el codigo del producto...")
            return codigo()


def nombre():
    nombre_producto= input("Ingrese el nombre del producto... " )
    opcion=input(f"El nombre ingresado es {nombre_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar el nombre del producto...")      
        return nombre()
    else:
        nombre_producto.lower
        return nombre_producto

def marca():
    marca_producto= input("Ingrese el nombre de la marca del producto... " )
    opcion=input(f"El nombre ingresado es {marca_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar la marca del producto...")    
        return marca()
    else:
        marca_producto.lower
        return marca_producto

def precio():
    precio_producto= input("Ingrese el precio del producto... " )
    opcion=input(f"El precio ingresado es {precio_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar el precio del producto...")
        return precio()
    else:
        if precio_producto.isdigit():
            return precio_producto
        else:
            print("Ingrese el precio del producto en numeros, vuleva a ingresar el precio del producto...")         
            return precio()

def stock():
    stock_producto= input("Ingrese la cantidad disponible del proucto... " )
    opcion=input(f"la cantidad ingresada es {stock_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar la cantidad disponible...")
        return stock()
    else:
        if stock_producto.isdigit():
            return stock_producto
        else:
            print("Ingrese el precio del producto en numeros, vuleva a ingresar la cantidad disponible...")
            return stock()

def color():
    color_producto= input("Ingrese el color del producto... " )
    opcion=input(f"El color ingresado es {color_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar el color del producto...")
        opcion=input("Presione enter para continuar...")        
        return color()
    else:
        color_producto.lower
        return color_producto

def caracteristicas():
    caracteristicas_producto= input("Ingrese las caracteristicas del producto... " )
    opcion=input(f"Usted ingreso lo siguiente:  {caracteristicas_producto}, si desea modificarlo presione ( n )  , de lo contrario enter")
    if opcion.lower() == "n":
        print("Vuleva a ingresar las caracteristicas del producto...")
        opcion=input("Presione enter para continuar...")      
        return caracteristicas_producto()
    else:
        caracteristicas_producto.lower
        return caracteristicas_producto


def agregar_productos():
    print("Agregue sus nuevos productos...")
    nuevo_producto = {
        "codigo_producto": codigo(),
        "nombre_producto": nombre(),
        "marca_producto": marca(),
        "precio_producto": precio(),
        "stock_producto": stock(),
        "color_producto": color(),
        "caracteristicas_producto": caracteristicas()
    }
    productos[nuevo_producto["codigo_producto"]] = nuevo_producto



agregar_productos()
