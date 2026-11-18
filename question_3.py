def minutos_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - minutos totales de cada usuario
    """
    minutos = {}

    for reproduccion in reproducciones:
        usuario = reproduccion["usuario"]
        # Si el usuario ya está, le sumamos los minutos; si no, lo agregamos
        if usuario in minutos:
            minutos[usuario] += reproduccion["minutos"]
        else:
            minutos[usuario] = reproduccion["minutos"]

    return minutos

def artistas_por_usuario(reprodicciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - lista de los artistas de cada usuario
    """
    artistas = {}

    for reproduccion in reprodicciones:
        usuario = reproduccion["usuario"]
        artista = reproduccion["artista"]
        # Si el usuario es nuevo, le creamos su lista vacía
        if usuario not in artistas:
            artistas[usuario] = []
        # Agregamos el artista solo si no estaba ya (para no repetirlo)
        if artista not in artistas[usuario]:
            artistas[usuario].append(artista)

    return artistas

def usuario_mas_activo(reproducciones: list) -> str:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        str: nombre del usuario con más minutos
    """
    # Reusamos la primera función para tener los minutos totales de cada uno
    minutos = minutos_por_usuario(reproducciones)

    mas_activo = ""
    mayor = -1
    for usuario in minutos:
        if minutos[usuario] > mayor:
            mayor = minutos[usuario]
            mas_activo = usuario

    return mas_activo


if __name__ == "__main__":
    reproducciones = [
        {"usuario" : "sofia" , "artista" : "Wolf Alice"   , "minutos" : 60 },
        {"usuario" : "daniel", "artista" : "Milo J"       , "minutos" : 30 },
        {"usuario" : "sofia" , "artista" : "Fleetwood Mac", "minutos" : 42 },
        {"usuario" : "carlos", "artista" : "Americania"   , "minutos" : 21 },
        {"usuario" : "elena" , "artista" : "Tame Impala"  , "minutos" : 25 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 56 },
        {"usuario" : "sofia" , "artista" : "MGMT"         , "minutos" : 43 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 20 }
    ]

    print(minutos_por_usuario(reproducciones))  # -> {“sofia” : 145, “daniel” : 30, “carlos” : 97, “elena” : 25} 
    print(artistas_por_usuario(reproducciones)) # -> {“sofia” : [“Wolf ALice”, “Fleetwood Mac”, MGMT],  
    #                                            #     “daniel” : [“Milo J”],  
    #                                            #     “carlos” : [“Americania”, “Dua Lipa”],  
    #                                            #     “elena”  : [“Tame Impala”]} 
    print(usuario_mas_activo(reproducciones))   # -> sofia
