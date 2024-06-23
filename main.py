#Sistema de control de invetario
import libreria.utilidades as utilidades
import libreria.inventario as inventario
menu = {
    1: "Agregar Producto",
    2: "Buscar Producto",
    3: "Mostrar Inventario",
    4: "Actualizar Cantidad", 
    5: "Eliminar",
    6: "Salir"
}
def main():
    option = None
    while not option:
        utilidades.clear()
        print("SISTEMA DE INVENTARIO")
        print('')
        for key, value in menu.items():
            print(f"{key} - {value}")

        option = input("Ingrese una opción: ")
        if not option.isdigit():
            print("Ingrese un número válido")
            option = None
            input("Presione enter para continuar...")
            continue
        option = int(option)
        if not option in menu:
            print("Ingrese una opción dentro del menú")
            option = None
            input("Presione enter para continuar...")
            continue
        if option == 6:
            exit()
        match option:
            case 1:
                inventario.add_producto()
            case 2:
                inventario.search_producto()
            case 3:
                inventario.show_productos()
            case 4:
                inventario.update_productos()
            case 5:
                inventario.delete_producto()
        option = None
              

main()