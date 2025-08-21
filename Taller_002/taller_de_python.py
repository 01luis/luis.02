import csv

def main():
    """
    Función principal que gestiona las operaciones con los datos de los clientes.
    """
    nombre_archivo = 'clientes.csv'
    
    # 1. Cargar los datos del archivo una sola vez
    clientes = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Omitir la fila de encabezados
            for fila in lector_csv:
                if len(fila) >= 3:
                    try:
                        saldo = float(fila[2])
                        clientes.append({'cedula': fila[0], 'nombre': fila[1], 'saldo': saldo})
                    except ValueError:
                        print(f"Advertencia: Saldo inválido en la fila: {fila}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Buscar saldo de un cliente")
        print("2. Contar clientes con saldos mayores a $50")
        print("3. Mostrar lista de clientes ordenada por saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_buscado = input("Ingrese el nombre del cliente: ").strip().lower()
            encontrado = False
            for cliente in clientes:
                if cliente['nombre'].strip().lower() == nombre_buscado:
                    print(f"El saldo de {cliente['nombre']} es: {cliente['saldo']:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"El cliente '{nombre_buscado}' no fue encontrado.")
        
        elif opcion == '2':
            contador = 0
            for cliente in clientes:
                if cliente['saldo'] > 50:
                    contador += 1
            print(f"Hay {contador} cliente(s) con saldos mayores a $50.")
        
        elif opcion == '3':
            clientes_ordenados = sorted(clientes, key=lambda x: x['saldo'])
            print("Listado de clientes ordenados ascendentemente por saldo:")
            for cliente in clientes_ordenados:
                print(f"  - {cliente['nombre']} (Saldo: {cliente['saldo']:.2f})")
        
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()