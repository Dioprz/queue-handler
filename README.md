# Sistema de Gestión de Turnos para Banco

Este sistema de gestión de turnos está diseñado para manejar eficientemente las
colas en un banco, priorizando a los clientes según su tipo (prioritario, buena
gente, normal) y manteniendo una relación 2:3 entre los clientes normales y
"buena gente".

## Características

- **Priorización de clientes:** Maneja tres tipos de clientes: prioritarios,
  buena gente y normales.
- **Relación 2:3:** Asegura una atención equitativa entre clientes normales y
  "buena gente", atendiendo 2 normales por cada 3 de buena gente.
- **Interfaz de usuario sencilla:** Menú interactivo para agregar turnos y
  atender al siguiente cliente.
- **Visualización del estado de las colas:** Muestra el número de turnos
  pendientes en cada cola.
- **Baterías incluidas:** El sistema inicia con turnos predefinidos en las colas
  para facilitar las pruebas.

## Estructura del Proyecto

- `main.py`: Contiene la lógica principal del programa, gestionando las colas y
  la interacción con el usuario.
- `printer.py`: Encargado de la presentación en pantalla: menús, mensajes y
  estado de las colas.
- `turn_handler.py`: Funciones para agregar turnos a las colas y determinar el
  siguiente turno a atender, manteniendo la relación 2:3.

## Cómo Utilizar

1. **Clonar el repositorio e instalar el paquete en un virtual environment:**

   ```bash
   git clone https://github.com/Dioprz/queue-handler
   cd queue-handler
   python3 -m venv .venv
   source .venv/bin/activate
   # source .venv/bin/activate.fish #if you use fish-shell
   pip install .
   python3 src/queue_handler/main.py
   ```

1. **Interactuar con el menú:**

   - **Opción 1:** Agregar un nuevo turno, seleccionando la prioridad del
     cliente.
   - **Opción 2:** Atender al siguiente cliente en la cola.
   - **Opción 3:** Salir del programa.

## Ejemplo de Uso

1. Ejecuta el programa.
1. Selecciona "1" para agregar un turno.
   1. Selecciona la prioridad del turno.
1. Agrega otro turno, esta vez de tipo "buena gente".
1. Selecciona "2" para atender un cliente.

## Consideraciones técnicas

- Se utiliza una estructura de datos `deque` para implementar las colas,
  permitiendo operaciones eficientes de agregar y quitar elementos.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE
para más detalles.
