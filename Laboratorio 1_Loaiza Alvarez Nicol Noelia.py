import random

# Crear el laberinto con paredes
def crear_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
    laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            fila_mapa_laberinto.append('#')
        laberinto.append(fila_mapa_laberinto)
        
# Mecanismo para llenar espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

# Mecanismo para que un caracter se desplaze de manera aleatoria
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    laberinto[fila_posicion_actual][columna_posicion_actual] = 'N'

# Generando espacios
    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1
            
    return laberinto

# Insertar filas, columnas y paredes
numero_filas = int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes

laberinto = crear_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)

for index, value in enumerate(laberinto):
    for index2, value2 in enumerate(value):
        if value2 == 'N':       
            posx=index
            posy=index2

# Generar movimiento aleatorio
for i in range(5):
# Si while True:
# Generara un movimiento aleatorio
#0 arriba
#1 abajo
#2 izquierda
#3 derecha
    mover = random.randrange(0,4)
    if mover == 0:
        print('arriba')
        if(laberinto[posx-1][posy] == ' '):
            laberinto[posx][posy] = ' '
            laberinto[posx-1][posy] = 'N'
            posx = posx-1
    
    if mover == 1:
        print('abajo')
        if(laberinto[posx+1][posy] == ' '):
            laberinto[posx][posy] = ' '
            laberinto[posx+1][posy] = 'N'
            posx = posx+1

    if mover == 2:
        print('izquierda')
        if(laberinto[posx][posy-1] == ' '):
            laberinto[posx][posy] = ' '
            laberinto[posx][posy-1] = 'N'
            posy = posy-1
    if mover == 3:
        print('derecha')
        if(laberinto[posx][posy+1] == ' '):
            laberinto[posx][posy] = ' '
            laberinto[posx][posy+1] = 'N'
            posy = posy+1

    for fila_mapa_laberinto in laberinto:
        print(fila_mapa_laberinto)
    