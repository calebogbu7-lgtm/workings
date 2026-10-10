import json
from pathlib import Path


def save_tickets(tickets, file_path="data/tickets.json"):
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)

def load_tickets(file_path="data/tickets.json"):
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            "Ticket data file contains invalid JSON."
        ) from error

    if not isinstance(tickets, list):
        raise ValueError("Ticket data must contain a JSON list.")

    return tickets