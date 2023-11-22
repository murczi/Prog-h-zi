#API-ok
#A diagrammok létrehozásához szükséges:
import matplotlib.pyplot as plt
#A diagrammok formázására szükséges:
import matplotlib.ticker as mticker
#Az adatok beolvasására szükséges:
import numpy as np
import pandas as pd
#Képek mentéséhez szükséges:
from PIL import Image

#A letöltött adatok beolvasása dataframe-be
df = pd.read_excel("stadat-okt0002-23.1.1.2-hu.xlsx", skiprows=1)

# Tengelyek és figure beállítása
fig, ax = plt.subplots()
x=df[df.columns[0]]

#------GDP------

#Formázás
#lépték beállítása
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax.yaxis.set_major_locator(mticker.MultipleLocator(100000))

#Tengelynevek beállítása
ax.ticklabel_format(useOffset=False, style='plain')
#Diagramcím
plt.title("A költségvetési intézmények oktatási kiadásai\na GDP százalékában")

#X tengely
plt.xlabel(df.columns[0])
ax.xaxis.set_label_coords(1.05, -0.025)
plt.xticks(rotation=45)

#Y tengely
plt.ylabel("GDP")

#GDP Diagram létrehozása
plt.plot(x,df[df.columns[len(df.columns)-1]])

#Diagram mentése és megnyitása képként
plt.savefig('GDP.png')
im = Image.open('GDP.png')
im.show()

#------Lineáris Diagram------

#Figure és tengelyek kiürítése
fig, ax = plt.subplots()

#Formázás
#lépték beállítása
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax.yaxis.set_major_locator(mticker.MultipleLocator(100000))

#Tengelynevek beállítása
ax.ticklabel_format(useOffset=False, style='plain')
#Diagramcím
plt.title("A költségvetési intézmények oktatási kiadásai\n(Lineáris)")

#X tengely
plt.xlabel(df.columns[0])
ax.xaxis.set_label_coords(1.05, -0.025)
plt.xticks(rotation=45)

#Y tengely
plt.ylabel("Millió Ft", rotation=0)
ax.yaxis.set_label_coords(-0.025,1)

#Lineáris regresszió diagram létrehozása iterációval
for i in range(1,len(df.columns)-1):
    plt.plot(x, df[df.columns[i]], label=df.columns[i])

#Jelmagyarázat létrehozása
plt.legend(loc='best')

#Diagram mentése és megnyitása képként
plt.savefig('Linear.png')
im = Image.open('Linear.png')
im.show()
#------Lineáris regresszió------

#Figure és tengelyek kiürítése
fig, ax = plt.subplots()

#Formázás
#lépték beállítása
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax.yaxis.set_major_locator(mticker.MultipleLocator(100000))

#Tengelynevek beállítása
ax.ticklabel_format(useOffset=False, style='plain')

#Diagramcím
plt.title("A költségvetési intézmények oktatási kiadásai\n(Lineáris regresszió)")

#X tengely
plt.xlabel(df.columns[0])
ax.xaxis.set_label_coords(1.05, -0.025)
plt.xticks(rotation=45)

#Y tengely
plt.ylabel("Millió Ft", rotation=0)
ax.yaxis.set_label_coords(-0.025,1)

#Lineáris regresszió diagram létrehozása iterációval
for i in range(1,len(df.columns)-1):
    plt.scatter(x, df[df.columns[i]])
    m, b = np.polyfit(x, df[df.columns[i]], 1)
    plt.plot(x, m * x + b, label=df.columns[i])

#Jelmagyarázat létrehozása
plt.legend(loc='best')

#Diagram mentése és megnyitása képként
plt.savefig('Linear_regression.png')
im = Image.open('Linear_regression.png')
im.show()