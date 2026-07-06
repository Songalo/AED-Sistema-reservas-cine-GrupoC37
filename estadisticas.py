from datos import peliculas, funciones, salas, limpiar, esperar_al_usuario

def tratar_estadisticas(opcion):
    if opcion == 1:
        print("Total de entradas vendidas")

    elif opcion == 2:
        print("Película más elegida")

    elif opcion == 3:
        print("Horario con mayor demanda")

    elif opcion == 4:
        print("Recaudación total")

    elif opcion == 5:
        print("Volviendo al menú principal...")

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
        except ValueError :
            print("Debe ingresar una opción del menú.")
            esperar_al_usuario()