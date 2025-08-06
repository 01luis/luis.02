ventas = []

while True:
    print("\n1. Nueva venta\n2. Listar ventas\n3. Buscar por ID\n4. Modificar\n5. Eliminar\n6. Total ingresos\n7. Salir")
    op = input("Opción: ")

    if op == "1":
        venta = [
            input("ID: "),
            input("Producto: "),
            input("Cantidad: "),
            input("Precio unitario: ")
        ]
        ventas.append(venta)
        print("Venta agregada.")
    
    elif op == "2":
        for v in ventas:
            print(f"ID:{v[0]} Producto:{v[1]} Cantidad:{v[2]} Precio:{v[3]}")
    
    elif op == "3":
        id_buscar = input("ID a buscar: ")
        encontrado = False
        for v in ventas:
            if v[0] == id_buscar:
                print("Venta:", v)
                encontrado = True
                break
        if not encontrado:
            print("No encontrada.")
    
    elif op == "4":
        id_mod = input("ID a modificar: ")
        for v in ventas:
            if v[0] == id_mod:
                v[1] = input("Nuevo producto: ")
                v[2] = input("Nueva cantidad: ")
                v[3] = input("Nuevo precio: ")
                print("Venta modificada.")
                break
        else:
            print("ID no encontrado.")
    
    elif op == "5":
        id_elim = input("ID a eliminar: ")
        ventas = [v for v in ventas if v[0] != id_elim]
        print("Venta eliminada (si existía).")
    
    elif op == "6":
        total = 0
        for v in ventas:
            try:
                total += int(v[2]) * float(v[3])
            except:
                print(f"Error con venta ID {v[0]}")
        print("Total ingresos: $", total)
    
    elif op == "7":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
