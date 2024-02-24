from flask import Blueprint, request, render_template
from utils import set, get
from datetime import datetime
from calendar import monthrange

calendarBlueprint = Blueprint("calendar", __name__)

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "january",
          "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]


@calendarBlueprint.route("/calendar", methods=["POST"])
def calendar():
    data = request.json
    text = data["text"]
    author = data["author"]

    date = datetime.today()
    today = int(date.strftime("%d"))

    for i, j in enumerate(MONTHS):
        if j in text.lower().split():
            date = date.replace(month=(i % 12) + 1)
            if datetime.today().month != date.month:
                today = -1
            break

    first = (int(date.replace(day=1).strftime("%w")) + 6) % 7
    month = [date.strftime("%B"), int(date.strftime("%m"))]
    monthlength = monthrange(date.year, date.month)[1] + 1

    user = get(author)
    if user == "Not Found":
        user = {
            "name": author,
            "events": []
        }
        set(author, user)

    events = []
    for i in range(1, monthlength):
        temp = []
        for event in user["events"]:
            time = datetime.strptime(event["time"], "%Y-%m-%d")
            if time.day + 1 == i and time.month == month[1]:
                temp.append({
                    "title": event["title"],
                    "location": event["location"]
                })
        events.append(temp)

    content = render_template(
        "calendar.html",
        user=user["name"],
        days=range(1, monthlength),
        start=first,
        month=month,
        today=today,
        events=events
    )

    message = {
        "text": content,
        "css": "/static/calendar.css"
    }

    return message
