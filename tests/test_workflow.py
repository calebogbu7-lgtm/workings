from campusflow.workflow import assign_ticket

ticket = {
    "id": "T001",
    "title": "Campus Wi-Fi is down",
    "status": "open",
    "assigned_to": None
}

assign_ticket(ticket, "Caleb")

print(ticket)

try:
    assign_ticket(ticket, "   ")
except ValueError as error:
    print(error)

from campusflow.workflow import update_status

ticket = {
    "id": "T002",
    "status": "open",
    "assigned_to": None
}

try:
    update_status(ticket, "in_progress")
except ValueError as error:
    print(error)

assign_ticket(ticket, "Caleb")

update_status(ticket, "in_progress")
print(ticket["status"])

update_status(ticket, "resolved")
print(ticket["status"])

update_status(ticket, "open")
print(ticket["status"])

from campusflow.workflow import get_work_queue

tickets = [
    {
        "id": "T001",
        "priority": "low",
        "status": "open"
    },
    {
        "id": "T002",
        "priority": "critical",
        "status": "open"
    },
    {
        "id": "T003",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": "T004",
        "priority": "medium",
        "status": "resolved"
    },
    {
        "id": "T005",
        "priority": "high",
        "status": "open"
    }
]

queue = get_work_queue(tickets)

for ticket in queue:
    print(ticket["id"], ticket["priority"], ticket["status"])

from campusflow.reports import generate_report

tickets = [
    {
        "id": "T001",
        "priority": "critical",
        "status": "open"
    },
    {
        "id": "T002",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": "T003",
        "priority": "medium",
        "status": "resolved"
    },
    {
        "id": "T004",
        "priority": "high",
        "status": "open"
    },
    {
        "id": "T005",
        "priority": "low",
        "status": "resolved"
    }
]

report = generate_report(tickets)

print(report)

empty_report = generate_report([])

print(empty_report)