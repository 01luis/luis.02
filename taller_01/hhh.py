ventas = []
next_id = 1

def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE VENTAS ---")
    print("1. Crear nueva venta")
    print("2. Listar todas las ventas")
    print("3. Buscar venta por ID")
    print("4. Modificar venta")
    print("5. Eliminar venta")
    print("6. Calcular total de ingresos")
    print("7. Salir")
    return input("Seleccione una opción: ")

def crear_venta():
    global next_id, ventas
    producto = input("Nombre del producto: ")
    
    try:
        cantidad = int(input("Cantidad vendida: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("Error: Cantidad y precio deben ser valores numéricos")
        return
    
    nueva_venta = [next_id, producto, cantidad, precio]
    ventas.append(nueva_venta)
    print(f"Venta creada exitosamente! ID: {next_id}")
    next_id += 1

def listar_ventas():
    if not ventas:
        print("No hay ventas registradas")
        return
    
    print("\n--- LISTADO DE VENTAS ---")
    for venta in ventas:
        print(f"ID: {venta[0]} | Producto: {venta[1]} | "
              f"Cantidad: {venta[2]} | Precio: ${venta[3]:.2f} | "
              f"Total: ${venta[2] * venta[3]:.2f}")

def buscar_venta():
    try:
        id_buscar = int(input("ID de la venta a buscar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero")
        return
    
    for venta in ventas:
        if venta[0] == id_buscar:
            print("\n--- VENTA ENCONTRADA ---")
            print(f"ID: {venta[0]}")
            print(f"Producto: {venta[1]}")
            print(f"Cantidad: {venta[2]}")
            print(f"Precio unitario: ${venta[3]:.2f}")
            print(f"Total: ${venta[2] * venta[3]:.2f}")
            return
    
    print(f"No se encontró ninguna venta con ID: {id_buscar}")

def modificar_venta():
    try:
        id_modificar = int(input("ID de la venta a modificar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero")
        return
    
    for venta in ventas:
        if venta[0] == id_modificar:
            print("\nVenta actual:")
            print(f"1. Producto: {venta[1]}")
            print(f"2. Cantidad: {venta[2]}")
            print(f"3. Precio unitario: ${venta[3]:.2f}")
            
            try:
                nuevo_producto = input("\nNuevo producto (Enter para mantener): ")
                nueva_cantidad = input("Nueva cantidad (Enter para mantener): ")
                nuevo_precio = input("Nuevo precio unitario (Enter para mantener): ")
                
                if nuevo_producto:
                    venta[1] = nuevo_producto
                if nueva_cantidad:
                    venta[2] = int(nueva_cantidad)
                if nuevo_precio:
                    venta[3] = float(nuevo_precio)
                
                print("Venta modificada exitosamente!")
                return
            except ValueError:
                print("Error: Cantidad y precio deben ser valores numéricos válidos")
                return
    
    print(f"No se encontró ninguna venta con ID: {id_modificar}")

def eliminar_venta():
    try:
        id_eliminar = int(input("ID de la venta a eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero")
        return
    
    for i, venta in enumerate(ventas):
        if venta[0] == id_eliminar:
            ventas.pop(i)
            print("Venta eliminada exitosamente!")
            return
    
    print(f"No se encontró ninguna venta con ID: {id_eliminar}")

def calcular_totales():
    total_ingresos = sum(venta[2] * venta[3] for venta in ventas)
    print(f"\n--- TOTAL DE INGRESOS ---")
    print(f"Ingresos totales: ${total_ingresos:.2f}")
    print(f"Cantidad de ventas registradas: {len(ventas)}")

# Programa principal
while True:
    opcion = mostrar_menu()
    
    if opcion == '1':
        crear_venta()
    elif opcion == '2':
        listar_ventas()
    elif opcion == '3':
        buscar_venta()
    elif opcion == '4':
        modificar_venta()
    elif opcion == '5':
        eliminar_venta()
    elif opcion == '6':
        calcular_totales()
    elif opcion == '7':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor seleccione 1-7")
