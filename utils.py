import requests

ROOT = "https://store.ncss.cloud/group3/planner/"


def set(key, val):
    response = requests.post(ROOT + key, json=val)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "Not Found"
    raise Exception


def get(key):
    response = requests.get(ROOT + key)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "Not Found"
    raise Exception


def delete(key):
    response = requests.delete(ROOT + key)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "Not Found"
    raise Exception


def createEvent(data, author):
    user = get(author)
    if user == "Not Found":
        user = {
            "name": author,
            "events": [data]
        }
    else:
        if data['title'] != '' or data['location'] != '':
            if data not in user["events"]:
                user["events"].append(data)
            else:
                return "At least one field is empety"
    set(author, user)

    message = {
        "text": f"Created task: {data['title']}"
    }

    return message
