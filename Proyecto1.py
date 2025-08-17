class Categoria:
    def __init__(self, codigo,nombre, precio, stock)
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock




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
            match

        case 2:
            print("Mostrar Productos")
        case 3:
            print("Buscar Producto")
        case 4:
            print("Gestion de Productos")
        case 5:
            print("Salir")