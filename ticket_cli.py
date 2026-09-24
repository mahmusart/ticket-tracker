# sample file to be deleted 
import json 
import os

TICKET_FILE = "tickets.json"

def load_tickets():
    if not os.path.exists(TICKET_FILE):
        return []
    with open(TICKET_FILE, "r") as f:
        return json.load(f)

def save_tickets(tickets):
    with open(TICKET_FILE, "w") as f:
        json.dump(tickets, f, indent=2)

def create_ticket():
    title = input("Ticket title: ")
    reporter = input("Reported by: ")
    priority = input("Priority (low/medium/high): ")

    return {
        "title":title,
        "reporter": reporter,
        "priority": priority,
        "status": "open"
    }

tickets = load_tickets()
tickets.append(create_ticket())
save_tickets(tickets)
print(f"Saved, You now have {len(tickets)} ticket(s).")



