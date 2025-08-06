
# Lista principal que almacenará todas las ventas
ventas = []

# Función para crear una nueva venta
def crear_venta():
    id = input("Ingrese ID de la venta: ")
    producto = input("Ingrese nombre del producto: ")
    cantidad = int(input("Ingrese cantidad vendida: "))
    precio_unitario = float(input("Ingrese precio unitario: "))
    venta = [id, producto, cantidad, precio_unitario]
    ventas.append(venta)
    print("✅ Venta creada con éxito.\n")

# Función para listar todas las ventas
def listar_ventas():
    if not ventas:
        print("❌ No hay ventas registradas.\n")
    else:
        for v in ventas:
            print(f"ID: {v[0]}, Producto: {v[1]}, Cantidad: {v[2]}, Precio: ${v[3]:.2f}")
        print()

# Función para buscar una venta por ID
def buscar_por_id():
    id_buscar = input("Ingrese el ID de la venta a buscar: ")
    for v in ventas:
        if v[0] == id_buscar:
            print(f"✅ Venta encontrada: {v}\n")
            return
    print("❌ Venta no encontrada.\n")

# Función para modificar una venta
def modificar_venta():
    id_modificar = input("Ingrese el ID de la venta a modificar: ")
    for i in range(len(ventas)):
        if ventas[i][0] == id_modificar:
            print("Ingrese los nuevos datos:")
            nuevo_producto = input("Nuevo producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio unitario: "))
            ventas[i] = [id_modificar, nuevo_producto, nueva_cantidad, nuevo_precio]
            print("✅ Venta modificada.\n")
            return
    print("❌ Venta no encontrada.\n")

# Función para eliminar una venta
def eliminar_venta():
    id_eliminar = input("Ingrese el ID de la venta a eliminar: ")
    for i in range(len(ventas)):
        if ventas[i][0] == id_eliminar:
            del ventas[i]
            print("✅ Venta eliminada.\n")
            return
    print("❌ Venta no encontrada.\n")

# Función para calcular el ingreso total
def calcular_totales():
    total = 0
    for v in ventas:
        total += v[2] * v[3]  # cantidad * precio_unitario
    print(f"💰 Ingreso total: ${total:.2f}\n")

# Menú principal en bucle
while True:
    print("===== MENÚ DE VENTAS =====")
    print("1. Crear nueva venta")
    print("2. Listar ventas")
    print("3. Buscar por ID")
    print("4. Modificar venta")
    print("5. Eliminar venta")
    print("6. Calcular ingreso total")
    print("7. Salir")
    
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == '1':
        crear_venta()
    elif opcion == '2':
        listar_ventas()
    elif opcion == '3':
        buscar_por_id()
    elif opcion == '4':
        modificar_venta()
    elif opcion == '5':
        eliminar_venta()
    elif opcion == '6':
        calcular_totales()
    elif opcion == '7':
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("❌ Opción inválida. Intente de nuevo.\n")
