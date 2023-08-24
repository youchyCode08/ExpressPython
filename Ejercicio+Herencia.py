#Vamos a crear una lista de tipos de producto de un centro comercial. Crearemos varios tipos de producto (alimento, electrodoméstico y moda)
#Daremos de alta varios objetos de cada tipo e inicializaremos los atributos propios de cada clase. 
#Crearemos un menú que muestre todos los objetos de cada tipo de producto, y permita vender alguno de ellos

class Producto:
    def __init__(self,referencia,nombre,pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp

    def __str__(self):
        return (self.referencia + " " + self.nombre + " " + self.pvp)

class Alimento(Producto):
    tipo = "alimento"
            
    def __str__(self):
        return (self.referencia + " " +self.tipo + " " + self.nombre + " " + self.pvp)

class Electrodomestico(Producto):
    tipo = "electrodoméstico"
    garantia = ""
            
    def __str__(self):
        return (self.referencia + " " +self.tipo + " " + self.nombre + " " + self.pvp + " " + self.garantia + "años de garantía")
        
class Moda(Producto):
    tipo = "moda"
    talla = ""
            
    def __str__(self):
        return (self.referencia + " " +self.tipo + " " + self.nombre + " " + self.pvp + " " + "talla " + self.talla)

manzana = Alimento('123782', 'Manzana golden', "2€")
pera = Alimento('982733', 'Pera conferencia', "1.5€")
lavadora = Electrodomestico('827318', 'Lavadora-secadora', "450€")
lavadora.garantia = "3"
nevera = Electrodomestico('123721', 'Nevera', "800€")
nevera.garantia = "4"
camisa = Moda('789415', 'Camisa vestir', "50€")
camisa.talla = "M"
pantalon = Moda('789415', 'Pantalón vestir', "50€")
pantalon.talla = "L"

alimentos = [manzana, pera]
electrodomesticos = [lavadora, nevera]
moda = [camisa, pantalon]

def listar(categoria):
    for producto in categoria:
        print(producto, "\n")

def comprar_producto(categoria):
    print("Elija un producto para comprar (Introduzca el código de referencia)")
    teclado = input()
    for producto in categoria:
        if producto.referencia == teclado:
            print("El producto " + producto.nombre + " se acaba de comprar\n")
            categoria.remove(producto)
            break
    else:
        print("El producto no existe")
                


while True:
    print("Bienvenido al centro comercial \nElija una de las siguientes opciones:\n1. Comprar alimentos\n2. Comprar electrodomésticos\n3. Comprar moda\n4. Salir")
    teclado = input()
    if teclado == "1":
        listar(alimentos)
        comprar_producto(alimentos)
    elif teclado == "2":
        listar(electrodomesticos)
        comprar_producto(electrodomesticos)
    elif teclado == "3":
        listar(moda)
        comprar_producto()
    elif teclado == "4":
        print("Terminando programa")
        break
    else:
        print("Opción incorrecta")
    
    
    
    