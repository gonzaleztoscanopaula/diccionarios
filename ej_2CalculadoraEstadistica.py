#Ejercicio2:
#Calculadora de Estadísticas de Números
#Escribe un programa que permita al usuario ingresar una lista de números y realice los
#siguientes cálculos estadísticos:
#1. Calcular la suma de los números.
#2. Calcular el promedio de los números.
#3. Encontrar el número mínimo y el número máximo de la lista.
#4. Calcular la desviación estándar de los números.
#El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
#luego imprimir los resultados de los cálculos estadísticos.


import math
numeroUsuario = input("Ingrese la lista de números separados por espacios: ")
numeros = [int(num) for num in numeroUsuario.split()]
print(f"Los números ingresados son: {numeros}")
numeros =list(numeros)

def calcular_suma():
    suma=0
    for num in numeros:
        suma=int(suma+int(num))
    print(f"La suma de los números ingresados es {suma}")
    return suma


def encontrar_numeroMinMax():
    numMax=0
    numMin=0
    for num in numeros:
        if num > numMax:
            numMax=num
        if numMin == 0 or num < numMin:
            numMin=num
    print(f"El numero mínimo es:  {numMin}")
    print(f"El numero máximo es:  {numMax}")
    return numMax, numMin

def promedio_Num():
    suma=0
    c=0
    promedioNum=0
    for numero in numeros:
        suma=int(suma+numero)
        c=c+1
        promedioNum=(suma/c)
    print(f"El promedio de los números es: {promedioNum}")
    return promedioNum


def calcularLaDesviacionEstandar():
    media = sum(numeros) / len(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    desviacion_estandar = math.sqrt(suma_cuadrados / len(numeros)) #math.sqrt se utiliza para calcular la raíz cuadrada y se aplica a la expresión correspondiente para obtener el valor final de la desviación estándar.
    print(f"La desviacion estandar de los numeros es: {desviacion_estandar}")
    return desviacion_estandar


while True:
    print("\n--- Calculadora ---")
    print("1. Calcular la suma de los números")
    print("2. Calcular el promedio de los números")
    print("3. Encontrar numero máximo y mínimo")
    print("4. Calcular la desviación estandar de los números")
    print("5. Obtener resultados calculados y salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        calcular_suma()
    elif opcion == "2":
        promedio_Num()
    elif opcion == "3":
        encontrar_numeroMinMax()
    elif opcion == "4":
        calcularLaDesviacionEstandar()
    elif opcion == "5":
        print("-----RESULTADOS-----")
        calcular_suma()
        encontrar_numeroMinMax()
        promedio_Num()
        calcularLaDesviacionEstandar()
        print("-----¡Gracias por utilizar el programa!-----")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.")