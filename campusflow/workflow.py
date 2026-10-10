def assign_ticket(ticket, staff_name):
    if not staff_name or not staff_name.strip():
        raise ValueError("Staff name cannot be empty.")

    ticket["assigned_to"] = staff_name.strip()

    return ticket

def update_status(ticket, new_status):
    allowed_statuses = ["open", "in_progress", "resolved"]

    if new_status not in allowed_statuses:
        raise ValueError("Invalid ticket status.")

    current_status = ticket["status"]

    allowed_transitions = {
        "open": ["in_progress"],
        "in_progress": ["resolved"],
        "resolved": ["open"]
    }

    if new_status not in allowed_transitions[current_status]:
        raise ValueError(
            f"Cannot change status from {current_status} to {new_status}."
        )

    if new_status == "in_progress" and not ticket["assigned_to"]:
        raise ValueError("Assign the ticket before starting work.")

    ticket["status"] = new_status

    return ticket

def get_work_queue(tickets):
    priority_order = {
        "critical": 0,
        "high": 1,
        "medium": 2,
        "low": 3
    }

    unresolved_tickets = []

    for ticket in tickets:
        if ticket["status"] != "resolved":
            unresolved_tickets.append(ticket)

    unresolved_tickets.sort(
        key=lambda ticket: (
            priority_order[ticket["priority"]],
            int(ticket["id"][1:])
        )
    )

    return unresolved_tickets