#PREGUNTA 5
def cuentadigitos(a,n):
  a = int(a)
  print(a)
  a = str(a)
  n = str(n)
  conteo = a.count(n)
  print(f"El dígito {n} aparece", conteo, "veces.") 
   
cuentadigitos(21311111,1) 
