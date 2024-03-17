#PREGUNTA 4
#Pido cantidad de alumnos del salón
n = int(input("ingrese la cantidad de alumnos: "))
#Creo diccionario donde se almacenará
listado = {}

#Creo tabla para ir asignando cada alumno a respectiva llave y colocar en lista las calificaciones.1
for i in range(n):
  alumno = input("ingrese el nombre del alumno: ")
  alumno = str(alumno)
  notitas = []
  for i in range(3):
      calif = input("colocar calificación en el curso: ")
      calif = int(calif)
      notitas.append(calif)
      listado[alumno] = notitas
print(listado)
