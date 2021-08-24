import random as r
import matplotlib.pyplot as plt

#Generar numero aleatorio.
print(r.randrange(10, 100))

lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista 1", lista)

r.shuffle(lista)
print(f"Lista 2", lista)

campana= [r.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()
