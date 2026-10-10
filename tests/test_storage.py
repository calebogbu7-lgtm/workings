from campusflow.storage import save_tickets, load_tickets
from tempfile import TemporaryDirectory
from pathlib import Path


with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "tickets.json"

    tickets = [
        {
            "id": "T001",
            "title": "Campus Wi-Fi is down",
            "status": "open"
        },
        {
            "id": "T002",
            "title": "Printer is not working",
            "status": "resolved"
        }
    ]

    save_tickets(tickets, file_path)

    loaded_tickets = load_tickets(file_path)

    print(loaded_tickets)
    print(tickets == loaded_tickets)

with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "missing.json"

    tickets = load_tickets(file_path)

    print(tickets)

with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "broken.json"

    file_path.write_text(
        "This is not valid JSON",
        encoding="utf-8"
    )

    try:
        load_tickets(file_path)
    except ValueError as error:
        print(error)