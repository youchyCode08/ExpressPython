nombres = ['Elisa', 'JUan', 'Alonso', 'julián']

for nombre in nombres:
    print(nombre)
    
a = {'nombre': 'Elisa', 'edad': 23}
b = {'nombre': 'Julián', 'edad': 22}

personas = []

personas.append(a)
personas.append(b)

for persona in personas:
    print(persona['nombre'], persona['edad'])

print(personas)