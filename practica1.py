#AAAA.
print(f"Nombre:")
nombre = input("")
print(f"Que tranza {nombre}")
print("Ah, {} vales pura madre.".format(nombre))

print(f"Edad:")
edad = input("")
print(f"Altura:")
altura = input("")

edad = int(edad)
if edad >= 18 and edad <= 100:
    print(f"Legal.")
elif edad >= 101:
    print(f"No we, eso no se puede")
else:
    print(f"Eres ilegal.")

altura = float(altura)
if altura >= 1.70 and altura <=1.99:
    print(f"Alto.")
elif altura >= 2.00:
    print(f"Poste")
elif altura >=1.55 and altura <=1.69:
    print(f"Tas chiquito.")
else:
    print(f"Te falta acido folico")

print(f"Mas weas.")
for i in range (0,10):
    print(i, )

