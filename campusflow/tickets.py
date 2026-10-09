def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"

    elif urgency == "high" or affected_users >= 10:
        return "high"

    elif urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"
    
def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Ticket title cannot be empty.")

    return title.strip()

def validate_category(category):
    allowed_categories = ["Network", "Hardware", "Software", "Other"]

    category = category.strip().capitalize()

    if category not in allowed_categories:
        raise ValueError("Invalid ticket category.")

    return category

def validate_urgency(urgency):
    allowed_urgencies = ["low", "medium", "high"]

    urgency = urgency.strip().lower()

    if urgency not in allowed_urgencies:
        raise ValueError("Invalid ticket urgency.")

    return urgency

def validate_affected_users(affected_users):
    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer.")

    return affected_users

def create_ticket(ticket_id, title, category, urgency, affected_users):
    title = validate_title(title)
    category = validate_category(category)
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    priority = calculate_priority(urgency, affected_users)

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }

    return ticket

def generate_ticket_id(tickets):
    highest_number = 0

    for ticket in tickets:
        ticket_id = ticket["id"]

        if ticket_id.startswith("T") and ticket_id[1:].isdigit():
            number = int(ticket_id[1:])

            if number > highest_number:
                highest_number = number

    return f"T{highest_number + 1:03d}"

def list_tickets(tickets):
    return tickets

def get_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    raise ValueError("Ticket not found.")