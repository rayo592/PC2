#PREGUNTA 6
def serie(nro_limit):
  nro_limit = int(nro_limit)
  val_fibo = []
  a = -1
  b = 1
  while b <= (nro_limit)- a:
    c = a +b 
    a = b
    b = c
    val_fibo.append(b)
  return print(val_fibo)
serie(1600)
