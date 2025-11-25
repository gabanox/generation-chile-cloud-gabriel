# Las funciones sirven para encapsular bloques repetitivos de código y reutilizarlos cuando sea necesario.
# Se crean utilizando la palabra clave 'def', seguida del nombre de la función y paréntesis. (Por ejemplo def hola() )
# Los argumentos o parámetros se colocan dentro de los paréntesis.
# Pueden devolver un valor utilizando la palabra clave 'return'.

# Ejemplo de una función que no recibe parámetros y no devuelve ningún valor


def saludo(nombre, edad):
    total_dias = calculo_anios_por_edad(edad)
    print(f"Hola, {nombre}! que bueno tenerte de regreso, han pasado {total_dias} desde que naciste")

def calculo_anios_por_edad(edad):
    dias_anio = 365
    dias_totales = dias_anio * edad
    return dias_totales

saludo("Gabriel", 42)





