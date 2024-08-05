""""
Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.
"""
nvendedor=str(input("Ingrese el nombre del vendedor")) #asignamos texto que queramos para el nombre del vendedor
sueldo=int(input("Ingrse el sueldo del vendedor")) #asignamos valor que queramos para el sueldo
vcomision=(int(input("Ingrese el valor de la comision de las ventas asignadas"))) #y asignamos el valor de la comision
stotal=sueldo+vcomision #aqui se saca el sueldo total, sumando sueldo y comision
print(f"El vendedor {nvendedor}, tiene un sueldo de {sueldo}, durante el mes obtuvo una comision de {vcomision} y el sueldo total: {stotal}") #lo que queremos mostrar en la consola