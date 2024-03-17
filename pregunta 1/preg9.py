#PREGUNTA 9 
def m(palabra):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #variable que irá almacenando las letras que no cumplan la condición de vocal
    no_vocal = ""   
    for i in palabra:       
        if i not in v:
            # Se añade a palabra que no contiene vocales si no se cumple condición
            no_vocal += i
    return no_vocal

texto = input("Ingrese una cadena de texto: ")
print("Texto sin vocales:", m(texto))

