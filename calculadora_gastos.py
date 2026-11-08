import os

def agregar_gasto(lista_gastos, descripcion, importe, categoria):
    gasto = {
        "descripcion": descripcion,
        "importe": importe,
        "categoria": categoria
    }

    lista_gastos.append(gasto)

def listar_gastos(lista_gastos):
    if not lista_gastos:
        print("No hay gastos registrados.")
        return

    print("\n--- Lista de gastos ---")

    for gasto in lista_gastos:
        print(f"Descripción: {gasto['descripcion']}, Importe: {gasto['importe']}, Categoria: {gasto['categoria']}")

def calcular_total(lista_gastos):
    return sum(gasto['importe'] for gasto in lista_gastos)

def filtrar_por_categoria(lista_gastos, categoria):
    gastos_filtrados = [gasto for gasto in lista_gastos if gasto['categoria'].lower() == categoria.lower()]

    return gastos_filtrados

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    lista_gastos = []

    while True:
        limpiar_pantalla()

        print("===================================")
        print("   CALCULADORA DE GASTOS   ")
        print("===================================")
        print("1. Añadir gasto")
        print("2. Listar todos los gastos")
        print("3. Ver total acumulado")
        print("4. Filtrar gastos por categoría")
        print("5. Salir")
        print("===================================")

        opcion = input("Seleccione una opción (1-5): ")

        match opcion:
            case "1":
                print("\n--- Añadir gasto ---")

                while True:
                    descripcion = input("Ingrese la descripción del gasto: ")

                    if descripcion:
                        break
                    print("La descripción no puede estar vacía. Ingrese una descripción válida.") 
                    
                while True:
                    try:
                        importe = float(input("Ingrese el importe del gasto: "))

                        if importe > 0:
                            break
                        else:
                            print("El importe no puede ser negativo.")
                    except ValueError:
                        print("Debe ingresar un número válido. No uses letras ni símbolos.")

                while True:
                    categoria = input("Ingrese la categoría del gasto: ")

                    if categoria:
                        break
                    print("La categoría no puede estar vacía. Ingrese una categoría válida.")

                agregar_gasto(lista_gastos, descripcion, importe, categoria)  

                print("\n¡Gasto guardado con éxito!")
                input("\nPresione Enter para volver al menú...")  

            case "2":
                print("\n--- Listar todos los gastos ---")

                listar_gastos(lista_gastos)

                input("\nPresione Enter para volver al menú...")
            case "3":
                print("\n--- Ver total acumulado ---")

                total = calcular_total(lista_gastos)

                print(f"Total acumulado de gastos: ${total:.2f}")

                input("\nPresione Enter para volver al menú...")
            case "4": 
                print("\n--- Filtrar gastos por categoría ---")

                categoria = input("Ingrese la categoría para filtrar: ")
                filtrados = filtrar_por_categoria(lista_gastos, categoria) 

                if not filtrados:
                    print(f"No hay gastos en la categoría '{categoria}'.")
                else:
                    for gasto in filtrados:
                        print(f"Descripción: {gasto['descripcion']}, Importe: {gasto['importe']}, Categoria: {gasto['categoria']}")

                input("\nPresione Enter para volver al menú...")

            case "5":
                print("\n--- Salir ---")
                print("¡Gracias por usar la calculadora! Saliendo...")
                break    
            case _:
                print("Opción no válida. Por favor, elige un número del 1 al 5.")
                input("\nPresione Enter para intentar de nuevo...")
    
if __name__ == "__main__":
    main() 