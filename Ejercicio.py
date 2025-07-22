ventas=[742,125,532,124,10,642,2643,6433,5432,124]
while True:
    print("\n------------------- MENÚ DE VENTAS --------------------\n1. Ingresar lista de ventas\n2. Mostrar todas las ventas ingresadas\n3. Calcular las venta más alta y la mas baja\n4. Calcular promedio de ventas\n5. Contar cuantos días superaron Q1000 en ventas\n6. Clasificar cada venta\n7. Salir")
    seleccion = input("Seleccione una opción: ")
    match seleccion:
        case "1":
            while True:
                try:
                    cant = int(input("Ingrese la cantidad de ventas que desea ingresar: "))
                    if cant<=0:
                        print("El valor debe ser positivo")
                    else:
                        break
                except:
                    print("El valor ingresado debe ser un número entero")

            for i in range(cant):
                while True:
                    try:
                        sale = int(input(f"Venta ingresada {i}:"))
                        if sale<=0:
                            print("El valor debe ser positivo")
                        ventas.append(sale)
                        break
                    except:
                        print("Ingrese un número entero")

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

            else:
                total = 0
                ammount = 0
                for i in ventas:
                    ammount += 1
                    total += i
                average = total / ammount
                print("El promedio de ventas es de Q" + round(average,2))


        case "5":
            if not ventas:
                print("No hay ventas")
            else:
                total2 = 0
                for venta in ventas:
                    if venta > 1000:
                        total2 += 1

                print(f"Un total de {total2} ventas superaron los Q1000")

        case "6":
            if not ventas:
                print("No hay ventas")
            else:
                high = []
                mid = []
                low = []
                for venta in ventas:
                    if venta > 1000:
                        high.append(venta)
                    elif venta > 500 and venta < 1000:
                        mid.append(venta)
                    else:
                        low.append(venta)

                print("\nVentas altas:")
                for i in high:
                    print("Q"+i)

                print("\nVentas medias:")
                for i in mid:
                    print("Q"+i)

                print("\nVentas bajas:")
                for i in low:
                    print("Q"+i)

        case "7":
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción inválida, intente nuevamente")