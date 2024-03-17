#PREGUNTA 7 
def pruebasiesprimo(g):
  g = int(g)

  esprimo = True
  primos= []
  no_primos= []
  for i in range(2,g):
    if g % i ==0:
      esprimo = False   
      no_primos.append(g)
      break
  if esprimo:
       print(f"El número {g} es primo")
  else:
      print(f"El número {g} no es primo")
  return esprimo
pruebasiesprimo(19)
