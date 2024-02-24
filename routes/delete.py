from flask import Blueprint, request
from utils import get, set

deleteBlueprint = Blueprint("delete", __name__)


@deleteBlueprint.route("/delete", methods=["POST"])
def deleteEvent():
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
                user["events"].pop(i)
                set(author, user)
                content = f"Event: <b>{event}</b> deleted."
                break
        else:
            content = f"Event: <b>{event}</b> not found."

    message = {
        "text": content
    }

    return message
