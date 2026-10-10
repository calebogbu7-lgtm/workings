
from campusflow.tickets import (
    create_ticket,
    generate_ticket_id,
    list_tickets,
    get_ticket
)

from campusflow.storage import load_tickets, save_tickets

from campusflow.workflow import (
    assign_ticket,
    update_status,
    get_work_queue
)

from campusflow.reports import generate_report
def handle_create_ticket(tickets):
    try:
        title = input("Enter ticket title: ")
        category = input("Enter category (Network, Hardware, Software, Other): ")
        urgency = input("Enter urgency (low, medium, high): ")
        affected_users = int(input("Enter number of affected users: "))

        ticket_id = generate_ticket_id(tickets)

        ticket = create_ticket(
            ticket_id,
            title,
            category,
            urgency,
            affected_users
        )

        tickets.append(ticket)
        save_tickets(tickets)

        print("\nTicket created successfully!")
        print(ticket)

    except ValueError as error:
        print(f"Error: {error}")
def show_menu():
    print("\n===== CampusFlow Helpdesk =====")
    print("1. Create a ticket")
    print("2. View all tickets")
    print("3. Assign a ticket")
    print("4. Update ticket status")
    print("5. View work queue")
    print("6. Generate report")
    print("7. Exit")


def main():
    tickets = load_tickets()

    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_create_ticket(tickets)
            

        elif choice == "2":
            all_tickets = list_tickets(tickets)

            if not all_tickets:
                print("No tickets found.")
            else:
                for ticket in all_tickets:
                    print(ticket)

        elif choice == "3":
            try:
                ticket_id = input("Enter ticket ID: ").strip()
                ticket = get_ticket(tickets, ticket_id)

                staff_name = input("Enter staff name: ")

                assign_ticket(ticket, staff_name)
                save_tickets(tickets)

                print("Ticket assigned successfully!")
                print(ticket)

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "4":
            try:
                ticket_id = input("Enter ticket ID: ").strip()
                ticket = get_ticket(tickets, ticket_id)

                new_status = input(
                    "Enter new status (in_progress or resolved): "
                ).strip()

                update_status(ticket, new_status)
                save_tickets(tickets)

                print("Ticket status updated successfully!")
                print(ticket)

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "5":
            work_queue = get_work_queue(tickets)

            if not work_queue:
                print("No unresolved tickets in the work queue.")
            else:
                print("\n===== CampusFlow Work Queue =====")

                for ticket in work_queue:
                    print(
                        f"ID: {ticket['id']} | "
                        f"Title: {ticket['title']} | "
                        f"Priority: {ticket['priority']} | "
                        f"Status: {ticket['status']} | "
                        f"Assigned to: {ticket['assigned_to']}"
                    )

        elif choice == "6":
            report = generate_report(tickets)

            print("\n===== CampusFlow Ticket Report =====")
            print(f"Total tickets: {report['total_tickets']}")

            print("\nTickets by status:")
            for status, count in report["by_status"].items():
                print(f"{status}: {count}")

            print("\nTickets by priority:")
            for priority, count in report["by_priority"].items():
                print(f"{priority}: {count}")

        elif choice == "7":
            print("Exiting CampusFlow. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()