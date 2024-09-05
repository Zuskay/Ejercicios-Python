# Solicita al usuario el número total de alumnos en el grupo
grupoAlumnos = int(input('Digite cuantos alumnos hay: '))

# Inicializa contadores y acumuladores para las edades
edadHombres = 0        # Suma de las edades de los hombres
edadMujeres = 0        # Suma de las edades de las mujeres
hombres = 0            # Contador de hombres
mujeres = 0            # Contador de mujeres

# Variables para almacenar los promedios de edad
promedioEdadHombres = 0
promedioEdadMujeres = 0

# Bucle para procesar la información de cada alumno
for i in range(grupoAlumnos):
    # Solicita al usuario el género del alumno (H para hombres, M para mujeres)
    genero = input(f'Ingrese el genero de la persona {i+1} (H/M): ')
    
    # Procesa la entrada según el género
    if genero.upper() == 'H':
        hombres += 1  # Incrementa el contador de hombres
        edadH = int(input('Ingrese la edad: '))  # Solicita la edad del hombre
        edadHombres += edadH  # Acumula la edad de los hombres
    elif genero.upper() == 'M':
        mujeres += 1  # Incrementa el contador de mujeres
        edadM = int(input('Ingrese la edad: '))  # Solicita la edad de la mujer
        edadMujeres += edadM  # Acumula la edad de las mujeres

# Calcula el promedio de edad de los hombres, si hay hombres en el grupo
if hombres > 0:
    promedioEdadHombres = edadHombres / hombres
else:
    promedioEdadHombres = 0

# Calcula el promedio de edad de las mujeres, si hay mujeres en el grupo
if mujeres > 0:
    promedioEdadMujeres = edadMujeres / mujeres
else:
    promedioEdadMujeres = 0

# Calcula el promedio de edad del grupo en general, si hay alumnos en el grupo
if grupoAlumnos > 0:
    promedioEdadGrupo = (edadHombres + edadMujeres) / grupoAlumnos
else:
    promedioEdadGrupo = 0

# Imprime los resultados
print(f'El promedio de la edad de los hombres es: {promedioEdadHombres:.2f} \n'
      f'El promedio de la edad de las mujeres es: {promedioEdadMujeres:.2f} \n'
      f'El promedio de la edad del grupo de alumnos es: {promedioEdadGrupo:.2f}')
