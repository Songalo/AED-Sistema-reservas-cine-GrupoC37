from datos import peliculas, funciones, salas, limpiar, espera_de_carga, esperar_al_usuario
from estadisticas import mostrar_estadisticas
from reservas import Iniciar_Reserva, cargar_reservas_json


def mostrar_menu():
    Menu = int(input("""
                ╔═══════════════════════════════════════════════════╗
                ║            Sistema de Reservas de Cine            ║
                ║═══════════════════════════════════════════════════║
                ║   1. Ver Cartelera                                ║
                ║   2. Ver funciones                                ║
                ║   3. Reservar Entradas                            ║
                ║   4. Ver Estadísticas                             ║
                ║   5. Salir                                        ║
                ║                                                   ║
                ╚═══════════════════════════════════════════════════╝
                Ingrese una opción: """))

    return Menu


def Mostrar_Cartelera():
    print("╔═══════════════════════════════════════════════════╗")
    print("║                     Cartelera                     ║")
    print("╚═══════════════════════════════════════════════════╝")
    print(f' {"ID":<2} | {"Película":<50} | {"Género":<15} | {"Duración":<8}')
    print("-" * 95)

    for i in range(len(peliculas)):
        print(
            f' {peliculas[i]["id"]:<2} |'
            f' {peliculas[i]["pelicula"]:<50} |'
            f' {peliculas[i]["genero"]:<15} |'
            f' {peliculas[i]["duracion"]} minutos'
        )

        espera_de_carga()

    esperar_al_usuario()
    limpiar()


def Mostrar_Funciones(reserva=0):
    reservas = cargar_reservas_json()

    print("╔═══════════════════════════════════════════════════╗")
    print("║                    Funciones                      ║")
    print("╚═══════════════════════════════════════════════════╝")
    print(
        f' {"ID":<3}| {"ID Pelicula":<15}| '
        f'{"Película":<45} | {"Sala":<15} | '
        f'{"Horario":<8} | {"Reservadas"}'
    )
    print("-" * 110)

    for i in range(len(funciones)):
        cantidad_reservada = 0

        for reserva_cargada in reservas:
            if reserva_cargada["id_funcion"] == funciones[i]["id"]:
                cantidad_reservada = (
                    cantidad_reservada
                    + reserva_cargada["cantidad"]
                )

        print(
            f' {funciones[i]["id"]:<3}| '
            f' {funciones[i]["pelicula_id"]:<14}|'
            f' {peliculas[funciones[i]["pelicula_id"] - 1]["pelicula"]:<45} |'
            f' {salas[funciones[i]["sala_id"] - 1]["nombre"]:<15} |'
            f' {funciones[i]["horario"]:<8} |'
            f' {cantidad_reservada}'
        )

        espera_de_carga()

    if reserva != 1:
        esperar_al_usuario()


def Menu_Reservas():
    Reserva = int(input("""
                ╔═══════════════════════════════════════════════════╗
                ║                     Reservas                      ║
                ║═══════════════════════════════════════════════════║
                ║   1. Iniciar nueva reserva                        ║
                ║   2. Volver al Menú Principal                     ║
                ║                                                   ║
                ╚═══════════════════════════════════════════════════╝
                Ingrese una opción: """))

    return Reserva


salir = True

while salir == True:
    limpiar()

    try:
        Menu = mostrar_menu()
        limpiar()

        if Menu == 1:
            Mostrar_Cartelera()

        elif Menu == 2:
            Mostrar_Funciones()

        elif Menu == 4:
            mostrar_estadisticas()
            esperar_al_usuario()

        elif Menu == 5:
            print("Saliendo...")
            salir = False

        if Menu == 3:
            limpiar()
            Reserva = Menu_Reservas()
            limpiar()

            if Reserva == 1:
                Iniciar_Reserva(Mostrar_Funciones)
                esperar_al_usuario()

            elif Reserva == 2:
                print("Volviendo al menú principal...")

    except ValueError:
        limpiar()
        print("Hubo un error, por favor escoja una de las opciones del menú.")
        input("Ingrese una tecla para continuar")

exit
