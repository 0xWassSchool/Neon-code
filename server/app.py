from flask import Flask, send_file
from api import theme, plugin


app = Flask(__name__)
app.register_blueprint(theme)
app.register_blueprint(plugin)


@app.route("/setup/normal", methods=["GET"])
def normal_setup():
    return send_file("./neon_editor.zip")


@app.route("/setup/developer", methods=["GET"])
def developer_setup():
    return send_file("./neon_editor_developer.zip")


if __name__ == "__main__":
    app.run()
