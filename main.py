from flask import Flask
from routes.calendar import calendarBlueprint
from routes.create import createBlueprint
from routes.get import getBlueprint
from routes.delete import deleteBlueprint

app = Flask("group3-planner")

app.register_blueprint(calendarBlueprint)
app.register_blueprint(createBlueprint)
app.register_blueprint(getBlueprint)
app.register_blueprint(deleteBlueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
