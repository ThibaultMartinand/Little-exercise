from random import *
#j'importe une librairie qui permet de tracer des graphiques
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery-nogrid')
#on définit 3 variables pour compter le nombre de fois qu'apparait chacun des résultats x pour le 4, y pour le -1 et z pour le 1
x=0
y=0
z=0
#on crée une boucle for qui va compter 1000 fois (i va prendre toutes les valeurs entre 0 et 999 dans cet exemple)
# ici on pourrait meme créer un input qui nous permettrait de parametrer nous meme le nombre d'itérations que l'on veut dans notre boucle for
# exemple ci dessous
itérations=input("Quel est le nombre d'itérations voulues ?")
for i in range(int(itérations)):
  B=randint(1,4)
  if B==1:
    J=randint(1,3)
    if J==1:
      G=4
      x+=1
    else:
      G=-1
      y+=1
  else:
    J=randint(1,3)
    if J==1:
      G=1
      z+=1
    else:
      G=-1
      y+=1
#on affiche les résultats des 3 variables que l'on vient de crée
print(x,y,z)
#on affiche le résultat le plus fréquent et son % d'apparition, sans suprise c'est le -1 (donc la variable y)  avec environ 67%
#la fonction prends comme valeur, la plus grande variable parmis les arguments qu'on lui donne
# la fonction int permet de convertir un chiffre en un entier (donc arrondir le pourcentage)
# il est possible de faire des calculs au sein meme de certaines fonctions comme c'est le cas avec la fonction int => je convertis le résultat en % directement dans le corps de la fonction
if max(x,y,z)==x :
    print("Le gain le plus fréquent est 4, il apparait ", int((x/1000)*100),"% du temps")
elif max(x,y,z)==y:
    print("Le gain le plus fréquent est -1, il apparait ", int((y/1000)*100),"% du temps")
elif max(x,y,z)==z :
    print("Le gain le plus fréquent est 1, il apparait ", int((z/1000)*100),"% du temps")

l=[x,y,z]
#ici on va tracer un camembert pour faire apparaitre les résultats
colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(l)))
fig, ax = plt.subplots()
ax.pie(l, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
