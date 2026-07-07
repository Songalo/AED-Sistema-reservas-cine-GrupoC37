import json
from datos import funciones, salas, peliculas

RUTA_JSON = "reservas_cargadas.json"

def cargar_reservas_json():
    """Lee las reservas desde el archivo JSON."""
    try:
        with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_reserva_json(nuevas_reservas):
    """Guarda la lista actualizada de reservas en el archivo JSON."""
    with open(RUTA_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(nuevas_reservas, archivo, indent=4, ensure_ascii=False)

def Iniciar_Reserva(Mostrar_Funciones):
    """Lógica para validar asientos y registrar una nueva reserva."""
    print("╔═══════════════════════════════════════════════════╗")
    print("║               Nueva Reserva de Entradas           ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    # Muestra las funciones en pantalla
    Mostrar_Funciones(reserva=1)
    print("\n")
    
    try:
        id_funcion = int(input("Ingrese el ID de la función que desea reservar: "))
        
        # Buscar si la función ingresada existe
        funcion_seleccionada = None
        for f in funciones:
            if f['id'] == id_funcion:
                funcion_seleccionada = f
                break
        
        if not funcion_seleccionada:
            print("❌ El ID de función ingresado no existe.")
            return

        # Cargamos el historial real del archivo JSON
        historial_reservas = cargar_reservas_json()
        asientos_ocupados = sum(r['cantidad'] for r in historial_reservas if r['id_funcion'] == id_funcion)

        # Buscar datos de la sala asociada
        sala_asociada = salas[funcion_seleccionada['sala_id'] - 1]
        asientos_disponibles = sala_asociada['capacidad'] - asientos_ocupados
        
        print(f"\nPelícula: {peliculas[funcion_seleccionada['pelicula_id'] - 1]['pelicula']}")
        print(f"Sala: {sala_asociada['nombre']} (Precio: ${sala_asociada['precio']})")
        print(f"Asientos disponibles: {asientos_disponibles}")
        
        if asientos_disponibles <= 0:
            print("❌ Lo sentimos, esta función se encuentra agotada.")
            return
            
        cantidad = int(input("\n¿Cuántas entradas desea reservar?: "))
        
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0.")
            return
            
        if cantidad > asientos_disponibles:
            print(f"❌ No hay suficientes asientos. Solo quedan {asientos_disponibles} disponibles.")
            return
            
        costo_total = cantidad * sala_asociada['precio']
        print(f"\nMonto Total a abonar: ${costo_total}")
        
        confirmar = input("¿Confirmar reserva? (S/N): ").strip().upper()
        
        if confirmar == 'S':
            # Generar ID autoincremental de forma dinámica basándonos en los datos del JSON
            nuevo_id = len(historial_reservas) + 1 if historial_reservas else 1
            
            nueva_reserva = {
                "id": nuevo_id,
                "id_funcion": id_funcion,
                "cantidad": cantidad
            }
            
            # Guardado real y persistencia en el archivo
            historial_reservas.append(nueva_reserva)
            guardar_reserva_json(historial_reservas)
            
            print(f"\n¡🎉 Reserva #{nuevo_id} guardada con éxito en el archivo JSON!")
        else:
            print("\nReserva cancelada.")
            
    except ValueError:
        print("❌ Error: Debe ingresar valores numéricos válidos.")
