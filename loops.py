total_venta = 0.0
frutas = [] 
(2*3)
def ingresar_productos():

    while True:
        nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")

        if nombre == "salir": # salir cuando el usuario ingrese 'salir'
            break
        precio = float(input(f"Ingresa el precio de {nombre}: "))

        fruta = {
            "nombre" :nombre,
            "precio" : precio
        }
        frutas.append(fruta)
        print(f"Ingresando la fruta: {nombre} con el precio de {precio}")

def imprimir_ticket():
    
    print("\n--- Ticket de Compra ---")
    for fruta in frutas:
        print(f"Fruta: {fruta['nombre']}, Precio: {fruta['precio']}")

if __name__ == "__main__":
    ingresar_productos()
    imprimir_ticket()
    