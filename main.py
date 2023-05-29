import pandas as pd
from pandas import ExcelWriter

from scraper import abrir_pagina,obtener_peliculas
from helpers import separar_info

#Flujo principal
abrir_pagina()
peliculas = obtener_peliculas()

#Convertir cada pelicula(texto) en una lista separada por datos como titulo,rate,comentarios,etc
lista_peliculas = []
for pelicula in peliculas:
    lista_peliculas.append(separar_info(pelicula))

for i in lista_peliculas:
    print(i)
    print(len(i))
    print()
    
#creemos nuestro dataset
df = pd.DataFrame(lista_peliculas,
                  columns=['Titulo and year','Duracion y genero','calificacion','label','metascore','Descripcion','Director y estrellas','votos'])

df.to_excel('peliculas.xlsx',index=False)



