#crearemos un ejercicio con el uso del if, elif, for while y un diccionario

# El Escenario: "La Tienda de Gadgets"
# Imagina que eres el administrador de una pequeña tienda. 
# Necesitas un programa que recorra tu inventario, v
# verifique existencias y permita realizar ventas 
# aplicando descuentos según la cantidad comprada.


#Estructura del Código
#Diccionario: Almacena los productos (clave) y su stock actual (valor).
#Bucle for: Para mostrar los productos disponibles al inicio.
#Bucle while: Para mantener el programa ejecutándose hasta que decidas salir.
#Condicionales if-elif-else: Para manejar la lógica de ventas y los niveles de stock.

# 1. El Diccionario: Producto -> Unidades disponibles
inventario = {
    "Laptop": 5,
    "Mouse": 15,
    "Teclado": 8,
    "Monitor": 3
}

print("--- BIENVENIDO AL SISTEMA DE INVENTARIO ---")

# 2. Bucle FOR: Mostrar productos actuales
print("\nProductos en existencia:")
for producto, stock in inventario.items():
    print(f"- {producto}: {stock} unidades")

# 3. Bucle WHILE: El programa sigue activo hasta que el usuario escriba 'salir'
activa = True
while activa:
    print("\n--- Menú de Ventas ---")
    seleccion = input("¿que producto desea vender? (o escriba 'salir' para terminar): ").capitalize()

    if seleccion == "Salir":
        activa = False
        print("Cerrando el sistema... ¡buen dia!")
    
    # 4. Uso del IF y ELIF para la lógica de negocio
    elif seleccion in inventario:
        cantidad = int(input(f"¿Cuántas unidades de {seleccion} desea vender?: "))
        stock_actual = inventario[seleccion]

        if cantidad > stock_actual:
            print(f"¡Error! No hay suficiente stock. Solo quedan {stock_actual}.")
        
        elif cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")

        else:
            # Procesar venta exitosa
            inventario[seleccion] -= cantidad
            print(f"Venta realizada. Nuevo stock de {seleccion}: {inventario[seleccion]}")
            
            # Mensaje especial si el stock es crítico
            if inventario[seleccion] == 0:
                print(f"AVISO: ¡El producto {seleccion} se ha agotado!")
    else:
        print("Ese producto no existe en nuestra base de datos.")

print("\nInventario finalizado.")