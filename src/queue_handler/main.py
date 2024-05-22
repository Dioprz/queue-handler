from collections import deque
from queue_handler import printer, turn_handler

if __name__ == "__main__":
    prior_deq = deque()
    kind_deq = deque()
    normal_deq = deque()

    # Creates a by default example
    prior_deq.extend((1, 2))
    kind_deq.extend((1, 2, 3, 4, 5))
    normal_deq.extend((1, 2, 3))

    prior_turn_counter = len(prior_deq)
    kind_turn_counter = len(kind_deq)
    normal_turn_counter = len(normal_deq)

    queues = {"prioritario": prior_deq, "buena_gente": kind_deq, "normal": normal_deq}

    client_type_selector = 0

    while True:
        printer.main_menu_header()
        printer.queues_overview(queues)
        user_command = printer.main_menu_options()

        if user_command == "3":
            break

        elif user_command == "1":
            priority = printer.priority_options()

            if priority == 1:
                prior_turn_counter += 1
                turn_handler.add_turn(prior_deq, prior_turn_counter)
            elif priority == 2:
                kind_turn_counter += 1
                turn_handler.add_turn(kind_deq, kind_turn_counter)
            elif priority == 3:
                normal_turn_counter += 1
                turn_handler.add_turn(normal_deq, normal_turn_counter)
            else:
                printer.priority_invalid_command()
                continue

        elif user_command == "2":
            turn, priority, client_type_selector = turn_handler.next_turn(
                queues, client_type_selector
            )
            if priority is not None:
                printer.attended_client(priority, turn)
            else:
                printer.no_clients_left()
            printer.back_to_main_menu()

        else:
            printer.main_menu_invalid_command()
