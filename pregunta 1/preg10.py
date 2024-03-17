#PREGUNTA 10
def k(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if "/" in fecha:
        #Formato MM/DD/AAAA
        mes, dia, anio = fecha.split("/")
    else:
        #Formato "Mes dia, año"
        mes_nombre, resto = fecha.split(" ", 1)
        mes = str(meses.index(mes_nombre) + 1)
        dia, anio = resto.split(", ")

    mes = mes.zfill(2)
    dia = dia.zfill(2)

    return f"{anio}-{mes}-{dia}"

ingresofecha = input("Ingrese una fecha en formato mes-día-año (MM/DD/AAAA) o Mes día, año: ")

# Convierto fecha en formato AAAA-MM-DD
fechanueva = k(ingresofecha)
print("La fecha en formato AAAA-MM-DD es:", fechanueva)