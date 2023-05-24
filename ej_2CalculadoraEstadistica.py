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

numeroUsuario =[]
def agregar_numeros():
    c=input("Ingrese la cantidad de números que va a cargar para realizar los cálculos: ")
    c=int(c)
    contador=1
    while contador<=c:    
        num = input(f"Ingrese el {contador}: numero... ")
        num=(int(num))
        numeroUsuario.append(num)
        contador+=1
    print(f"Los números ingresados son {numeroUsuario}")


def calcular_suma():
    suma=0
    for num in numeroUsuario:
        suma=int(suma+num)
    print(f"La suma de los números ingresados es {suma}")




def encontrar_numeroMinMax():
    numMax=0
    numMin=0
    for num in numeroUsuario:
        if num > numMax:
            numMax=num
        if numMin == 0 or num < numMin:
            numMin=num
    print(f"El numero mínimo es:  {numMin}")
    print(f"El numero máximo es:  {numMax}")

def promedioNum():
    suma=0
    c=0
    promedioNum=0
    for numero in numeroUsuario:
        suma=int(suma+numero)
        c=c+1
        promedioNum=(suma/c)
    print(f"El promedio de los números es: {promedioNum}")


while True:
    print("\n--- Calculadora ---")
    print("1. Agregar 10 números")
    print("2. Calcular la suma de los números")
    print("3. Encontrar numero máximo y mínimo")
    print("4. Calcular el promedio de los números")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_numeros()
    elif opcion == "2":
        calcular_suma()
    elif opcion == "3":
        encontrar_numeroMinMax()
    elif opcion == "4":
        promedioNum()
    elif opcion == "5":
        print("¡Hasta la vista baby!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.")
