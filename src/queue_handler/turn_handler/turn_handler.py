def add_turn(queue, turn_number):
    queue.append(turn_number)


def next_turn(queue, client_type_selector):
    """
    Para conservar la relación 2:3 entre clientes normales y buena gente, se hace uso de un contador que sirve para seleccionar qué tipo de cliente se atenderá. De esta forma los clientes normales se priorizaran cuando el selector sea 0 o 1, y los clientes buena gente se priorizarán cuando el selector sea 2, 3 o 4.

    El estado del selector se actualiza adecuadamente en cada atención de un cliente.
    """
    prioritario = queue["prioritario"]
    buena_gente = queue["buena_gente"]
    normal = queue["normal"]

    if prioritario:
        turno = prioritario.popleft()
        return turno, "prioritario", client_type_selector

    elif buena_gente and normal:
        if client_type_selector in {0, 1}:
            turno = normal.popleft()
            prioridad = "cliente normal"
            client_type_selector = (client_type_selector + 1) % 5
        else:
            turno = buena_gente.popleft()
            prioridad = "buena gente"
            client_type_selector = (client_type_selector + 1) % 5
        return turno, prioridad, client_type_selector

    elif buena_gente:
        turno = buena_gente.popleft()
        if client_type_selector in {2, 3, 4}:
            client_type_selector = (client_type_selector + 1) % 5
        return turno, "buena gente", client_type_selector

    elif normal:
        turno = normal.popleft()
        if client_type_selector in {0, 1}:
            client_type_selector = (client_type_selector + 1) % 5
        return turno, "cliente normal", client_type_selector

    else:
        return None, None, client_type_selector
