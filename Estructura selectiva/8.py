<<<<<<< HEAD
# Solicita la edad, la unidad de edad (en años o meses), el nivel de hemoglobina y el sexo del usuario
edad = float(input("Ingrese su edad (en años o meses): "))
unidad_edad = input("¿La edad ingresada es en años o meses? (ingrese 'años' o 'meses'): ").strip().lower()
nivel_hemoglobina = float(input("Ingrese su nivel de hemoglobina (g%): "))
sexo = input("Ingrese su sexo (mujer/hombre): ").strip().lower()

# Determina si la persona tiene anemia basado en la edad, nivel de hemoglobina y sexo
def determinar_anemia(edad, unidad_edad, nivel_hemoglobina, sexo):
    if unidad_edad == "meses":
        if edad <= 1:
            if 13 <= nivel_hemoglobina <= 26:
                return "Negativo"
            else:
                return "Positivo"
        elif 1 < edad <= 6:
            if 10 <= nivel_hemoglobina <= 18:
                return "Negativo"
            else:
                return "Positivo"
        elif 6 < edad <= 12:
            if 11 <= nivel_hemoglobina <= 15:
                return "Negativo"
            else:
                return "Positivo"
        else:
            return "Edad en meses no válida. Debe ser de 0 a 12 meses."
    elif unidad_edad == "años":
        if 1 < edad <= 5:
            if 11.5 <= nivel_hemoglobina <= 15:
                return "Negativo"
            else:
                return "Positivo"
        elif 5 < edad <= 10:
            if 12.6 <= nivel_hemoglobina <= 15.5:
                return "Negativo"
            else:
                return "Positivo"
        elif 10 < edad <= 15:
            if 13 <= nivel_hemoglobina <= 15.5:
                return "Negativo"
            else:
                return "Positivo"
        elif edad > 15:
            if sexo == "mujer":
                if 12 <= nivel_hemoglobina <= 16:
                    return "Negativo"
                else:
                    return "Positivo"
            elif sexo == "hombre":
                if 14 <= nivel_hemoglobina <= 18:
                    return "Negativo"
                else:
                    return "Positivo"
            else:
                return "Sexo no válido. Debe ser 'mujer' o 'hombre'."
        else:
            return "Edad en años no válida. Debe ser mayor a 1 año."
    else:
        return "Unidad de edad no válida. Debe ser 'años' o 'meses'."

# Determina el resultado
resultado = determinar_anemia(edad, unidad_edad, nivel_hemoglobina, sexo)

# Imprime el resultado
=======
# Solicita la edad, la unidad de edad (en años o meses), el nivel de hemoglobina y el sexo del usuario
edad = float(input("Ingrese su edad (en años o meses): "))
unidad_edad = input("¿La edad ingresada es en años o meses? (ingrese 'años' o 'meses'): ").strip().lower()
nivel_hemoglobina = float(input("Ingrese su nivel de hemoglobina (g%): "))
sexo = input("Ingrese su sexo (mujer/hombre): ").strip().lower()

# Determina si la persona tiene anemia basado en la edad, nivel de hemoglobina y sexo
def determinar_anemia(edad, unidad_edad, nivel_hemoglobina, sexo):
    if unidad_edad == "meses":
        if edad <= 1:
            if 13 <= nivel_hemoglobina <= 26:
                return "Negativo"
            else:
                return "Positivo"
        elif 1 < edad <= 6:
            if 10 <= nivel_hemoglobina <= 18:
                return "Negativo"
            else:
                return "Positivo"
        elif 6 < edad <= 12:
            if 11 <= nivel_hemoglobina <= 15:
                return "Negativo"
            else:
                return "Positivo"
        else:
            return "Edad en meses no válida. Debe ser de 0 a 12 meses."
    elif unidad_edad == "años":
        if 1 < edad <= 5:
            if 11.5 <= nivel_hemoglobina <= 15:
                return "Negativo"
            else:
                return "Positivo"
        elif 5 < edad <= 10:
            if 12.6 <= nivel_hemoglobina <= 15.5:
                return "Negativo"
            else:
                return "Positivo"
        elif 10 < edad <= 15:
            if 13 <= nivel_hemoglobina <= 15.5:
                return "Negativo"
            else:
                return "Positivo"
        elif edad > 15:
            if sexo == "mujer":
                if 12 <= nivel_hemoglobina <= 16:
                    return "Negativo"
                else:
                    return "Positivo"
            elif sexo == "hombre":
                if 14 <= nivel_hemoglobina <= 18:
                    return "Negativo"
                else:
                    return "Positivo"
            else:
                return "Sexo no válido. Debe ser 'mujer' o 'hombre'."
        else:
            return "Edad en años no válida. Debe ser mayor a 1 año."
    else:
        return "Unidad de edad no válida. Debe ser 'años' o 'meses'."

# Determina el resultado
resultado = determinar_anemia(edad, unidad_edad, nivel_hemoglobina, sexo)

# Imprime el resultado
>>>>>>> e202adae2eba232c5ee50d165221f050486cdf8d
print(f"Resultado de anemia: {resultado}")