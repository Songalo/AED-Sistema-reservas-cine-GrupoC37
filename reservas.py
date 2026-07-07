import json
from datos import funciones, salas, peliculas


RUTA_JSON = "reservas_cargadas.json"


def cargar_reservas_json():
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_reserva_json(nuevas_reservas):
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(nuevas_reservas, archivo, indent=4, ensure_ascii=False)


def Iniciar_Reserva(Mostrar_Funciones):
    print("╔═══════════════════════════════════════════════════╗")
    print("║               Nueva Reserva de Entradas           ║")
    print("╚═══════════════════════════════════════════════════╝")

    Mostrar_Funciones(reserva=1)
    print("\n")

    try:
        id_funcion = int(input("Ingrese el ID de la función que desea reservar: "))

        funcion_seleccionada = None

        for funcion in funciones:
            if funcion["id"] == id_funcion:
                funcion_seleccionada = funcion
                break

        if not funcion_seleccionada:
            print("El ID de función ingresado no existe.")
            return

        historial_reservas = cargar_reservas_json()
        asientos_ocupados = 0

        for reserva in historial_reservas:
            if reserva["id_funcion"] == id_funcion:
                asientos_ocupados = asientos_ocupados + reserva["cantidad"]

        sala_asociada = salas[funcion_seleccionada["sala_id"] - 1]
        asientos_disponibles = sala_asociada["capacidad"] - asientos_ocupados

        print(
            f"\nPelícula: "
            f"{peliculas[funcion_seleccionada['pelicula_id'] - 1]['pelicula']}"
        )
        print(
            f"Sala: {sala_asociada['nombre']} "
            f"(Precio: ${sala_asociada['precio']})"
        )
        print(f"Asientos disponibles: {asientos_disponibles}")

          if asientos_disponibles <= 0:
            print("Lo sentimos, esta función se encuentra agotada.")
            return

        print("\nPromociones disponibles:")
        print("3 entradas: 10% de descuento")
        print("4 entradas o más: 20% de descuento")

        cantidad = int(input("\n¿Cuántas entradas desea reservar?: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if cantidad > asientos_disponibles:
            print(
                f"No hay suficientes asientos. "
                f"Solo quedan {asientos_disponibles} disponibles."
            )
            return

        costo_total = cantidad * sala_asociada["precio"]

        if cantidad >= 4:
            descuento = costo_total * 0.20
            costo_total = costo_total - descuento
            print("\nPromoción aplicada: 20% de descuento.")

        elif cantidad == 3:
            descuento = costo_total * 0.10
            costo_total = costo_total - descuento
            print("\nPromoción aplicada: 10% de descuento.")

        print(f"\nMonto total a abonar: ${costo_total}")

        confirmar = input("¿Confirmar reserva? (S/N): ").strip().upper()

        confirmar = input("¿Confirmar reserva? (S/N): ").strip().upper()

        if confirmar == "S":
            nuevo_id = len(historial_reservas) + 1

            nueva_reserva = {
                "id": nuevo_id,
                "id_funcion": id_funcion,
                "cantidad": cantidad
            }

            historial_reservas.append(nueva_reserva)
            guardar_reserva_json(historial_reservas)

            print("\nReserva realizada con éxito.")
        else:
            print("\nReserva cancelada.")

    except ValueError:
        print("Debe ingresar un valor numérico.")
