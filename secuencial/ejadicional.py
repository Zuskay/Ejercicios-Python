nestudiante=str(input("Ingrese el nombre del estudiante")) #asignamos el nombre del estudiante
cpromedio=int(input("Ingrese la calificacion promedio de las actividades realizadas en clase")) #asignamos calificacion promedio de las actividades realizadas en clase
cpromedio= cpromedio*0.3 #saco el 30% de las actividades 
cproyectof=int(input("Ingrese la calificacion del proyecto final")) #asigno valor de la calificacion del proyecto final
cproyectof= cproyectof*0.5 #saco el 50% de la calificacion del proyecto final
cevaluaciones=int(input("Ingrese la calificacion promedio de las evaluaciones parciales")) #asigno valor de la calificacion de las evaluaciones
cevaluaciones= cevaluaciones*0.2 #saco el 20% de las notas de las evaluaciones

total= cpromedio+cproyectof+cevaluaciones #se realiza el total de las notas

print(f"La nota final de algoritmia del estudiante {nestudiante} es: {total}") #lo que se muestra en consola


