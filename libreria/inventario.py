import libreria.utilidades as utilidades
inventario = [{
        "nombre": 'Harina Pan',
        "precio": 1.3,
        "cantidad": 40
    },{
        "nombre": "Arroz",
        "precio": 1.0,
        "cantidad": 20
    }
]

def add_producto():
    nombre = input("Ingrese nombre del producto: ").title()
    for i in inventario:
        if i["nombre"] == nombre:
            input("Producto ya existe dentro de inventario(enter para continuar...)")
            return
        
    precio = float(input("Ingrese precio $: "))
    cant = int(input("Ingrese cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cant
    }
    inventario.append(producto)
    print("Producto agregado con exito")
    input("Presione enter para continuar...")
    return 

def search_producto():
    dato = input("Ingrese el nombre del producto: ").title()
    resultado = list(filter(lambda elemento: elemento["nombre"].startswith(dato), inventario))
    utilidades.clear()
    for producto in resultado:
        print(f'Nombre: {producto["nombre"]}\nPrecio: {producto["precio"]}$\nCantidad: {producto["cantidad"]} ')
        print("==============")
    input("Presione enter para continuar...")

def show_productos():
    utilidades.clear()
    print("Productos Registrados\n")
    for producto in inventario:
        print(f'Nombre: {producto["nombre"]}\nPrecio: {producto["precio"]}$\nCantidad: {producto["cantidad"]} ')
        print("==============")
    input("Presione enter para continuar...")
    return

def update_productos():
    for producto in inventario:
        print(f'Nombre: {producto["nombre"]}\nPrecio: {producto["precio"]}$\nCantidad: {producto["cantidad"]} ')
        print("==============")
        
    nombre = input("Ingrese el nombre del producto que desea actualizar: ").title()
    for producto in inventario:
        if producto["nombre"] == nombre:
            nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombre}: $"))
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {nombre}: "))

            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad

            print(f"Producto {nombre} actualizado con éxito.")
            input("Presione enter para continuar...")
            return

    print(f"No se encontró el producto con nombre {nombre}.")
    input("Presione enter para continuar...")

def delete_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ").title()

    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado con éxito.")
            input("Presione enter para continuar...")
            return

    print(f"No se encontró el producto {nombre}.")
    input("Presione enter para continuar...")
