from datos import peliculas, funciones, salas, limpiar, esperar_al_usuario
from reservas import cargar_reservas_json


def total_entradas_vendidas():
    reservas = cargar_reservas_json()
    total = 0

    for reserva in reservas:
        total = total + reserva["cantidad"]

    print("Total de entradas vendidas:", total)


def pelicula_mas_elegida():
    reservas = cargar_reservas_json()
    entradas_por_pelicula = {}

    for reserva in reservas:
        id_funcion = reserva["id_funcion"]
        cantidad = reserva["cantidad"]

        for funcion in funciones:
            if funcion["id"] == id_funcion:
                id_pelicula = funcion["pelicula_id"]

                if id_pelicula in entradas_por_pelicula:
                    entradas_por_pelicula[id_pelicula] = (
                        entradas_por_pelicula[id_pelicula] + cantidad
                    )
                else:
                    entradas_por_pelicula[id_pelicula] = cantidad

                break

    if len(entradas_por_pelicula) == 0:
        print("No hay reservas cargadas.")
    else:
        id_mas_elegida = max(
            entradas_por_pelicula,
            key=entradas_por_pelicula.get
        )

        for pelicula in peliculas:
            if pelicula["id"] == id_mas_elegida:
                print("Película más elegida:", pelicula["pelicula"])
                print(
                    "Entradas vendidas:",
                    entradas_por_pelicula[id_mas_elegida]
                )
                break


def horario_mayor_demanda():
    reservas = cargar_reservas_json()
    entradas_por_horario = {}

    for reserva in reservas:
        id_funcion = reserva["id_funcion"]
        cantidad = reserva["cantidad"]

        for funcion in funciones:
            if funcion["id"] == id_funcion:
                horario = funcion["horario"]

                if horario in entradas_por_horario:
                    entradas_por_horario[horario] = (
                        entradas_por_horario[horario] + cantidad
                    )
                else:
                    entradas_por_horario[horario] = cantidad

                break

    if len(entradas_por_horario) == 0:
        print("No hay reservas cargadas.")
    else:
        horario_mas_elegido = max(
            entradas_por_horario,
            key=entradas_por_horario.get
        )

        print("Horario con mayor demanda:", horario_mas_elegido)
        print(
            "Entradas vendidas:",
            entradas_por_horario[horario_mas_elegido]
        )


def recaudacion_total():
    reservas = cargar_reservas_json()
    total_recaudado = 0

    for reserva in reservas:
        if "importe" in reserva:
            total_recaudado = total_recaudado + reserva["importe"]
        else:
            id_funcion = reserva["id_funcion"]
            cantidad = reserva["cantidad"]

            for funcion in funciones:
                if funcion["id"] == id_funcion:
                    id_sala = funcion["sala_id"]

                    for sala in salas:
                        if sala["id"] == id_sala:
                            total_recaudado = (
                                total_recaudado
                                + cantidad * sala["precio"]
                            )
                            break

                    break

    print("Recaudación total: $", total_recaudado)


def tratar_estadisticas(opcion):
    if opcion == 1:
        total_entradas_vendidas()

    elif opcion == 2:
        pelicula_mas_elegida()

    elif opcion == 3:
        horario_mayor_demanda()

    elif opcion == 4:
        recaudacion_total()

    elif opcion == 5:
        print("Volviendo al menú principal...")

    else:
        print("La opción ingresada no es válida.")


def menu_estadisticas():
    opcion = int(input("""
                ╔═══════════════════════════════════════════╗
                ║                Estadísticas               ║
                ║═══════════════════════════════════════════║
                ║   1. Total de entradas vendidas           ║
                ║   2. Película más elegida                 ║
                ║   3. Horario con mayor demanda            ║
                ║   4. Recaudación total                    ║
                ║   5. Volver al Menú Principal             ║
                ║                                           ║
                ╚═══════════════════════════════════════════╝
                Ingrese una opción: """))

    return opcion


def mostrar_estadisticas():
    en_estadisticas = True

    while en_estadisticas:
        limpiar()

        try:
            opcion = menu_estadisticas()
            limpiar()

            if opcion == 5:
                en_estadisticas = False
            else:
                tratar_estadisticas(opcion)
                esperar_al_usuario()

        except ValueError:
            print("Debe ingresar una opción numérica.")
            esperar_al_usuario()
