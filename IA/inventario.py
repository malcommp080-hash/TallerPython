def mostrar_menu():
    print("\n=== Inventario Básico ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")
    return input("Selecciona una opción (1-4): ")

def ejecutar_inventario():

    inventario = []

    while True:
        opcion = mostrar_menu()

        # --- OPCIÓN 1: AGREGAR PRODUCTO ---
        if opcion == "1":
            print("\n[1. Agregar producto]")
            nombre = input("Nombre del producto: ").strip().lower()
            
            # Validación de entrada para la cantidad
            try:
                cantidad = int(input("Cantidad (entero): "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a 0.")
                    continue
            except ValueError:
                print("⚠️ Error: Debes ingresar un número entero válido.")
                continue

            # Buscar si el producto ya existe en la lista de listas
            encontrado = False
            for producto in inventario:
                if producto[0] == nombre:
                    producto[1] += cantidad  # Aumentar el stock existente
                    print(f"🔄 El producto '{nombre}' ya existe. Stock actualizado. Nueva cantidad: {producto[1]}")
                    encontrado = True
                    break
            
            # Si no existe, se crea un registro nuevo
            if not encontrado:
                inventario.append([nombre, cantidad])
                print(f"✅ Producto '{nombre}' agregado exitosamente al inventario.")

        # --- OPCIÓN 2: MOSTRAR INVENTARIO ---
        elif opcion == "2":
            print("\n[2. Mostrar inventario]")
            if not inventario:
                print("El inventario está vacío actualmente.")
            else:
                print("-" * 35)
                print(f"{'PRODUCTO':<20} | {'CANTIDAD':<10}")
                print("-" * 35)
                # Al no repetir nombres en la Opción 1, se muestra la lista sin duplicados
                for producto in inventario:
                    print(f"{producto[0].capitalize():<20} | {producto[1]:<10}")
                print("-" * 35)

        # --- OPCIÓN 3: VENDER PRODUCTO ---
        elif opcion == "3":
            print("\n[3. Vender producto]")
            if not inventario:
                print("⚠️ No hay productos en el inventario para realizar ventas.")
                continue

            nombre_buscar = input("Nombre del producto a vender: ").strip().lower()
            encontrado = False

            # Buscar el producto usando su índice para poder retirarlo si es necesario
            for i, producto in enumerate(inventario):
                if producto[0] == nombre_buscar:
                    encontrado = True
                    try:
                        print(f"Stock disponible de '{nombre_buscar}': {producto[1]}")
                        cant_vender = int(input("¿Cuántas unidades deseas vender?: "))
                        
                        if cant_vender <= 0:
                            print("⚠️ La cantidad a vender debe ser mayor a 0.")
                            break
                        if cant_vender > producto[1]:
                            print("⚠️ No hay suficiente stock para realizar esta venta.")
                            break
                        
                        # Actualizar cantidad en el inventario
                        producto[1] -= cant_vender
                        print(f"🛒 Venta realizada: Se vendieron {cant_vender} unidades de '{nombre_buscar}'.")
                        
                        # Si el stock llega a 0, se retira por completo de la lista
                        if producto[1] == 0:
                            inventario.pop(i)
                            print(f"🗑️ El producto '{nombre_buscar}' se ha quedado sin stock y fue retirado de la lista.")
                            
                    except ValueError:
                        print("⚠️ Error: Ingresa un número entero válido.")
                    break

            if not encontrado:
                print(f"❌ El producto '{nombre_buscar}' no se encuentra en el inventario.")

        # --- OPCIÓN 4: SALIR ---
        elif opcion == "4":
            print("\n👋 Saliendo del sistema de inventario. ¡Hasta luego!")
            break
        
        else:
            print("⚠️ Opción inválida. Por favor, selecciona un número del 1 al 4.")

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_inventario()