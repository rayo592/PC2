#PREGUNTA 3

pares= []
impares= []
while True:
    respuesta = input("¿Desea ingresar un número?: ").lower()  # Convertimos la entrada a minúsculas
    
    if respuesta == "si":
        numero = int(input("Ingrese el número: "))
        
        # Verificamos si el número es par o impar y actualizamos las variables correspondientes
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    elif respuesta == "no":
        break 
    else:
        print("Por favor, ingrese una respuesta válida (si o no).")

# Muestro la cantidad de números pares e impares
print(pares)
print(impares)

cant_pares = len(pares)
cant_impares = len(impares)
print(f"la cantidad de números pares es : {cant_pares}")
print(f"la cantidad de números impares es: {cant_impares}")
