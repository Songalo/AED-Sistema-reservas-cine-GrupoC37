from os import system
from time import sleep
from msvcrt import getch

def limpiar() :
    system('cls')

def espera_de_carga() :
    sleep(0.5)

def esperar_al_usuario() :
    print('Toque cualquier tecla para volver al Menú')
    getch()

peliculas = [
        {
            'id' : 1,
            'pelicula' : "Scary Movie: Terrorificamente Incorrecta",
            'genero' : "Comedia",
            'duracion' : 100
        },
        {
            'id' : 2,
            'pelicula' : "Backrooms: Sin Salida",
            'genero' : "Terror",
            'duracion' : 110
        },
        {
            'id' : 3,
            'pelicula' : "Toy Story 5",
            'genero' : "Aventura",
            'duracion' : 102
        },
        {
            'id' : 4,
            'pelicula' : "Spider-Man: Mas Allá del Spider-Verso",
            'genero' : "Acción",
            'duracion' : 140
        },
        {
            'id' : 5,
            'pelicula' : "Five Nights at Freddy's 2" ,
            'genero' : "Terror",
            'duracion' : 104
        },
        {
            'id' : 6,
            'pelicula' : "Oppenheimer" ,
            'genero' : "Suspenso",
            'duracion' : 180
        },
        {
            'id' : 7,
            'pelicula' : "Avatar: El camino del agua" ,
            'genero' : "Acción",
            'duracion' : 192
        }
]

funciones = [
    {
        'id' : 1,
        'pelicula_id' : 2,
        'sala_id' : 1,
        'reservadas' : 0,
        'horario' : "16:30"
    },
    {
        'id' : 2,
        'pelicula_id' : 5,
        'sala_id' : 2,
        'reservadas' : 0,
        'horario' : "16:30"
    },
    {
        'id' : 3,
        'pelicula_id' : 6,
        'sala_id' : 3,
        'reservadas' : 0,
        'horario' : "17:30"
    },
    {
        'id' : 4,
        'pelicula_id' : 3,
        'sala_id' : 1,
        'reservadas' : 0,
        'horario' : "19:00"
    },
    {
        'id' : 5,
        'pelicula_id' : 1,
        'sala_id' : 2,
        'reservadas' : 0,
        'horario' : "19:00"
    },
    {
        'id' : 6,
        'pelicula_id' : 7,
        'sala_id' : 3,
        'reservadas' : 0,
        'horario' : "21:00"
    },
    {
        'id' : 7,
        'pelicula_id' : 4,
        'sala_id' : 1,
        'reservadas' : 0,
        'horario' : "22:00"
    },
    {
        'id' : 8,
        'pelicula_id' : 4,
        'sala_id' : 2,
        'reservadas' : 0,
        'horario' : "22:00"
    }
]

salas = [
    {
        'id': 1,
        'nombre' : 'Sala 2D',
        'tipo' : '2D',
        'capacidad': 80,
        'precio' : 4000
    },
    {
        'id': 2,
        'nombre' : 'Sala 3D',
        'tipo' : '3D',
        'capacidad': 70,
        'precio' : 5000
    },
    {
        'id': 3,
        'nombre' : 'Sala IMAX',
        'tipo' : 'IMAX',
        'capacidad': 50,
        'precio' : 7000
    }
]
