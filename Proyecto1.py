class Ingreso:
    def __init__(self, codigo,nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(f"El codigo ingresado es: {self.codigo}, el nombre del producto: {self.nombre}, con precio de {self.precio}, el stock de {self.stock} ")

class Registrar_Producto:
    def __init__(self):
        self.producto = {}

    def agregar_producto(self):
        while True:
            try:
                codigo = int(input("Ingresa el codigo del producto: "))
                if codigo in self.producto:
                    print("El codigo del producto ya existe.")
                    error = input("Presione ENTER para ingresar nuevamente o 0 para salir:")
                    if error == "0":
                        break
                    else:
                        continue
                nombre_producto = input("Ingresa el nombre del producto: ")
                precio_producto = input("Ingresa el precio del producto: ")
                stock_producto = input("Ingresa el stock del producto: ")
                self.producto[codigo] = Ingreso(codigo, nombre_producto, precio_producto, stock_producto)
                print("Producto registrado correctamente.")

            except ValueError:
                print("No se puedo agregar un producto")
                continue





opcion = 0
while opcion != 5:
    print("Bienvenidos a la tienda de Ropa ")
    print("1.- Registrar Producto")
    print("2.- Mostrar Productos")
    print("3.- Buscar Producto")
    print("4.- Gestion de Productos")
    print("5.- Salir")
    opcion = int(input("seleccione una de las opciones que desee: "))

    match opcion:
        case 1:
            print("Registrar Producto")
            print("A continuacion se le presenta las Categorias disponibles")
            print("1.- Playeras")
            print("2.- Pantalones")
            print("3.- Sueteres")
            print("4.- Zapatos")
            categoria = int(input("seleccione una de las opciones: "))

        case 2:
            print("Mostrar Productos")
        case 3:
            print("Buscar Producto")
        case 4:
            print("Gestion de Productos")
        case 5:
            print("Salir")