from flask import Blueprint, request, render_template
from utils import createEvent, get

createBlueprint = Blueprint("create", __name__)


@createBlueprint.route("/create", methods=["POST"])
def create():
    data = request.json
    author = data["author"]

    menu = render_template("userInterface/menu.html")
    create = render_template("userInterface/create.html")
    query = render_template("userInterface/query.html")

    if "form_data" in data:
        if "option" in data['form_data']:
            if data['form_data']['option'] == "plan":
                message = {'text': create,
                           'state': data['form_data']['option']}
            else:
                message = {'text': query, 'state': data['form_data']['option']}
            return message
        else:
            if 'location' in data['form_data']:
                res = createEvent(data['form_data'], author)
            else:
                user = get(author)
                print(data['form_data'])
                content = f"Event: <b>{data['form_data']['title']}</b> not found."
                if user == "Not Found":
                    user = {
                        "name": author,
                        "events": []
                    }
                    set(author, user)
                else:
                    for i, j in enumerate(user["events"]):
                        if j["title"] == data['form_data']['title']:
                            content = render_template(
                                "event.html",
                                title=j["title"],
                                location=j["location"],
                                time=j["time"],
                            )
                            break
                message = {
                    "text": content
                }
                return message
            return res
    else:
        return {'author': 'Planner bot', 'text': menu, 'state': 'initial'}
