ventas=[]
while True:
    print("\n------------------- MENÚ DE VENTAS --------------------\n1. Ingresar lista de ventas\n2. Mostrar todas las ventas ingresadas\n3. Calcular las venta más alta y la mas baja\n4. Calcular promedio de ventas\n5. Contar cuantos días superaron Q1000 en ventas\n6. Clasificar cada venta\n7. Salir")
    seleccion = input("Seleccione una opción: ")
    match seleccion:
        case "1":
            while True:
                try:
                    cant = int(input("Ingrese la cantidad de ventas que desea ingresar: "))
                    break
                except:
                    print("El valor ingresado debe ser un número")

            for i in range(cant):
                while True:
                    try:
                        sale = int(input(f"Venta ingresada{i}:"))
                        ventas.append(sale)
                        break
                    except:
                        print("Ingrese un número")

        case "2":
            if not ventas:
                print("No hay ventas")
            else:
                for i in ventas:
                    print(f"Venta {i+1}: {ventas[i]}")

        case "3":
            if not ventas:
                print("No hay ventas")
            else:
                print(f"Venta más alta: {max(ventas)}")
                print(f"Venta más baja: {min(ventas)}")

        case "4":
            if not ventas:
                print("No hay ventas")

        case "5":
            pass

        case "6":
            pass

        case "7":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida, intente nuevamente")