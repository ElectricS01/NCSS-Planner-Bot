from flask import Blueprint, request, render_template
from utils import get, set

getBlueprint = Blueprint("get", __name__)


@getBlueprint.route("/get", methods=["POST"])
def getEvent():
    data = request.json
    author = data["author"]
    event = data["params"]["event"]

    user = get(author)
    if user == "Not Found":
        user = {
            "name": author,
            "events": []
        }
        set(author, user)
        content = f"Event: <b>{event}</b> not found."
    else:
        for i, j in enumerate(user["events"]):
            if j["title"] == event:
                content = render_template(
                    "event.html",
                    title=j["title"],
                    location=j["location"],
                    time=j["time"],
                )
                break
        else:
            content = f"Event: <b>{event}</b> not found."

    message = {
        "text": content
    }

    return message


@getBlueprint.route("/get/all", methods=["POST"])
def getAllEvents():
    data = request.json
    author = data["author"]

    user = get(author)
    if user == "Not Found":
        user = {
            "name": author,
            "events": []
        }
        set(author, user)
        content = f"No events found for <b>{author}</b>."
    else:
        if len(user["events"]) == 0:
            content = f"No events found for <b>{author}</b>."
        else:
            content = render_template(
                "events.html",
                user=author,
                events=user["events"],
            )

    message = {
        "text": content
    }

    return message
