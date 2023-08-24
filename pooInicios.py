class Coche:
    marca = 'Nissan'
    
    def acelerar(self, a):
        print("Acelerando...")
        
a = 3
coche1 = Coche()
coche1.color = 'Azul'
coche1.puertas = 4
coche1.modelo = 'Altima'
coche1.acelerar(a)

print(coche1.modelo)
    