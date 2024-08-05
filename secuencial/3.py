"""
Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los
números ingresado es: xxxx
"""

n1=int(input("Ingrese el primer numero")) #asignamos valor numerico que queramos a la variable con el input
n2=int(input("Ingrese el segundo numero")) #asignamos valor numerico que queramos a la variable con el input
n3=int(input("Ingrese el tercer numero")) #asignamos valor numerico que queramos a la variable con el input
promedio=(n1+n2+n3)/3 #sacamos el promedio de los tres numeros que asignamos anteriormente
print(f"El promedio de los numeros ingresados es: {promedio}") #Lo que muestra la consola