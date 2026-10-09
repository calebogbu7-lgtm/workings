from campusflow.tickets import calculate_priority

print(calculate_priority("high", 15))
print(calculate_priority("high", 5))
print(calculate_priority("low", 12))
print(calculate_priority("medium", 5))
print(calculate_priority("low", 4))
print(calculate_priority("low", 1))

from campusflow.tickets import validate_title

print(validate_title("Campus Wi-Fi is down"))
print(validate_title("  Printer is not working  "))

try:
    validate_title("   ")
except ValueError as error:
    print(error)

from campusflow.tickets import validate_category

print(validate_category("Network"))
print(validate_category("  HARDWARE  "))
print(validate_category("software"))

try:
    validate_category("Electricity")
except ValueError as error:
    print(error)

from campusflow.tickets import validate_urgency

print(validate_urgency("HIGH"))
print(validate_urgency(" medium "))
print(validate_urgency("low"))

try:
    validate_urgency("urgent")
except ValueError as error:
    print(error)
from campusflow.tickets import validate_affected_users

print(validate_affected_users(15))
print(validate_affected_users(1))

try:
    validate_affected_users(0)
except ValueError as error:
    print(error)

try:
    validate_affected_users(2.5)
except ValueError as error:
    print(error)

try:
    validate_affected_users("five")
except ValueError as error:
    print(error)

from campusflow.tickets import create_ticket

ticket = create_ticket(
    "T001",
    "Campus Wi-Fi is down",
    "NETWORK",
    "HIGH",
    15
)

print(ticket)

from campusflow.tickets import generate_ticket_id

tickets = []

first_id = generate_ticket_id(tickets)
print(first_id)

tickets.append({"id": first_id})

second_id = generate_ticket_id(tickets)
print(second_id)

tickets.append({"id": second_id})

third_id = generate_ticket_id(tickets)
print(third_id)

tickets = [
    {
        "id": "T001",
        "title": "Campus Wi-Fi is down"
    },
    {
        "id": "T002",
        "title": "Printer is not working"
    }
]

from campusflow.tickets import list_tickets, get_ticket

tickets = [
    {
        "id": "T001",
        "title": "Campus Wi-Fi is down"
    },
    {
        "id": "T002",
        "title": "Printer is not working"
    }
]

print(list_tickets(tickets))

ticket = get_ticket(tickets, "T002")
print(ticket)

try:
    get_ticket(tickets, "T003")
except ValueError as error:
    print(error)