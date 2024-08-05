"""
Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
de la compra el valor del descuento y el valor final a pagar. 
"""
vcompra=int(input("Ingrese el valor de la compra")) #En esta variable asignamos el valor que queramos de la compra con el input
descuento=int(input("Cual es el descuento")) #asignamos el valor del descuento que queramos con un input

total=vcompra-((vcompra*descuento)/100) #operacion para tener el valor final, osea el valor de la compra con el descuento asignado
total = int (total) #para que el total sea numero entero
print(f"La compra fue de {vcompra}, con un descuento del {descuento}% y el valor final a pagar es {total}") #lo que se quiere mostrar en la consola