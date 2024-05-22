def main_menu_header():
    print("\n\n\n\n----------------------------------------")
    print("Gestor de turnos")
    print("----------------------------------------")


def queues_overview(queues):
    prioritario = queues["prioritario"]
    buena_gente = queues["buena_gente"]
    normal = queues["normal"]
    print("Estado de las colas:")
    print(f"  Prioritario: {len(prioritario)} turnos")
    print(f"  Buena gente: {len(buena_gente)} turnos")
    print(f"  Cliente normal: {len(normal)} turnos")


def main_menu_options():
    print("\nOpciones:")
    print("1. Agregar nuevo turno")
    print("2. Siguiente turno por atender")
    print("3. Salir")

    return input("Ingrese su opción (1-3): ")


def main_menu_invalid_command():
    print("\n\nComando inválido. Por favor, ingrese un número entre 1 y 3.")
    back_to_main_menu()


def priority_options():
    print("\n----------------------------------------")
    print("Seleccione la prioridad del nuevo turno:")
    print("1. Prioritario")
    print("2. Buena gente")
    print("3. Cliente normal")

    return int(input("Ingrese la prioridad del nuevo turno (1-3): "))


def priority_invalid_command():
    print("Comando inválido. Regresando al menú inicial")


def attended_client(priority, turn):
    print("\n----------------------------------------")  # Separador visual
    print(f"Turno {priority} número {turn} atendido.")


def no_clients_left():
    print("\n----------------------------------------")  # Separador visual
    print("No hay turnos pendientes.")


def back_to_main_menu():
    print("\nPresione enter para volver al menú inicial")
    input()
