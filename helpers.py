#Le pasamos el texto de una pelicula y esta funcion lo separa a una lista donde cada elemento
#sera un dato de la pelicula
def separar_info(pelicula):
    pelicula_separada = pelicula.split("\n")
    return pelicula_separada