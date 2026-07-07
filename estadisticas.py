from datos import peliculas, funciones, salas, limpiar, esperar_al_usuario
from reservas import cargar_reservas_json


def tratar_estadisticas(opcion):
    
    reservas = cargar_reservas_json()

    # Cuenta si se encuentran reservas ya hechas anteriormente

    if len(reservas) == 0:
        print("Todavía no hay reservas cargadas.")
        return

    if opcion == 1:
        total = 0
        # Suma el total de reservas vendidas
        for reserva in reservas:
            total += reserva["cantidad"]

        print(f"Total de entradas vendidas: {total}")
        
    elif opcion == 2:
        contador_peliculas = {}
        # Inicializa el contador
        for pelicula in peliculas:
            contador_peliculas[pelicula["id"]] = 0
        # Hace recuento de la cantidad de reservas para cada película
        for reserva in reservas:
            for funcion in funciones:
                if funcion["id"] == reserva["id_funcion"]:
                    contador_peliculas[funcion["pelicula_id"]] += reserva["cantidad"]
                    break
        # Halla la película con más cantidad de reservas
        id_mas_elegida = max(contador_peliculas, key=contador_peliculas.get)

        pelicula = peliculas[id_mas_elegida - 1]
        # Imprime la película mas elegida con su total de entradas reservadas
        print(f"Película más elegida: {pelicula['pelicula']}")
        print(f"Entradas reservadas: {contador_peliculas[id_mas_elegida]}")

    elif opcion == 3:
        contador_horarios = {}
        # Inicializa contador
        for funcion in funciones:
            contador_horarios[funcion["horario"]] = 0
        # Hace un recuento de las reservas en todos los horarios disponibles
        for reserva in reservas:
            for funcion in funciones:
                if funcion["id"] == reserva["id_funcion"]:
                    contador_horarios[funcion["horario"]] += reserva["cantidad"]
                    break
        # Halla el horario donde hubo mayor demanda
        horario_mayor = max(contador_horarios, key=contador_horarios.get)
        # Imprime el horario con mayor demandas y el total de entradas reservadas
        print(f"Horario con mayor demanda: {horario_mayor}")
        print(f"Entradas reservadas: {contador_horarios[horario_mayor]}")

    elif opcion == 4:
        recaudacion = 0
        
        for reserva in reservas:
            for funcion in funciones:
                if funcion["id"] == reserva["id_funcion"]: # Halla la función que se reservó
                    sala = salas[funcion["sala_id"] - 1] # Se halla la sala en donde se dará la función
                    recaudacion += reserva["cantidad"] * sala["precio"] # Se multiplica la cantidad de reservas por el precio de la sala
                    break
        print(f"Recaudación total: ${recaudacion}")
        # Imprime la recaudación total

    elif opcion == 5:
        print("Volviendo al menú principal...")

    else:
        print("La opción ingresada no es válida.")


def menu_estadisticas():
    opcion = int(input("""
╔═══════════════════════════════════════════════════╗
║                   Estadísticas                    ║
║═══════════════════════════════════════════════════║
║   1. Total de entradas vendidas                   ║
║   2. Película más elegida                         ║
║   3. Horario con mayor demanda                    ║
║   4. Recaudación total                            ║
║   5. Volver al Menú Principal                     ║
╚═══════════════════════════════════════════════════╝
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
