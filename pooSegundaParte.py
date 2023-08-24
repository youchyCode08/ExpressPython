class Coche:
    pass 

    #método constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    #método para la consola
    def __str__(self):
        return ("\nMarca: " +self.marca+ " \nModelo: " +self.modelo+ " \nColor: " +self.color)
coche1 = Coche('Nissan', 'Altima', 'Negro' )
print(coche1)

class Consecionario:
    
    def __init__(self, coches = []):
        self.coches = coches
        
    
    #método para mostrar los coches en la terminal    
    def mostrar_coches(self):
        for coche in self.coches:
            print("Marca: " +coche.marca+ " \nModelo: " +coche.modelo+ " \nColor: " +coche.color)

coche1 = Coche(' Ford', ' Fiesta', ' Azul')
coche2 = Coche(' Nissan', ' Versa', ' Gris')
coche3 = Coche(' Volkswagen', ' Getta', ' Rojo')

consecionario1 = Consecionario(coches=[coche1, coche2, coche3])
consecionario1.mostrar_coches()

        
        

        