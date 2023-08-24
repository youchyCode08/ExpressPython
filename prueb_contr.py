nombre = "Javier"
edad = 25

if nombre == "Elena" and edad == 23:
    print("Su nombre es", nombre, "tiene edad de ", edad)
elif nombre != "Elena" and edad == 23:
    print("No te llamas elena pero tienes 23 años")
elif nombre == "Elena" and edad != 23:
    print("te llamas elena pero no tienes 23 años")
else:
    print("no te llamas elena ni tienes 23 años")