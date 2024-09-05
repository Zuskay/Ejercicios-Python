# Importa el módulo random para poder generar selecciones aleatorias
import random

# Solicita al usuario el total de la compra y lo convierte a un entero
totalCompra = int(input("¿Cuál fue el total de la compra?: "))

# Define una lista de colores que representan las balotas disponibles
color = ["rojo", "verde", "negra"]

# Selecciona aleatoriamente uno de los colores de la lista
colorAleatorio = random.choice(color)

# Evalúa el color seleccionado y aplica descuentos o muestra el total de la compra según el color de la balota
if colorAleatorio == "rojo":
    # Si la balota es roja, se aplica un descuento del 15%
    print("Ganaste un descuento del 15% por obtener una balota roja")
    # Calcula el valor final de la compra después de aplicar el descuento
    print(f"El valor final de la compra es de {totalCompra - (totalCompra * 0.15)}")
elif colorAleatorio == "verde":
    # Si la balota es verde, se aplica un descuento del 20%
    print("Ganaste un descuento del 20% por obtener una balota verde")
    # Calcula el valor final de la compra después de aplicar el descuento
    print(f"El valor final de la compra es de {totalCompra - (totalCompra * 0.2)}")
elif colorAleatorio == "negra":
    # Si la balota es negra, no se aplica descuento
    print("No ganaste ningún descuento por obtener una balota negra")
    # Muestra el valor final de la compra sin descuento
    print(f"El valor final de la compra es de {totalCompra}")
