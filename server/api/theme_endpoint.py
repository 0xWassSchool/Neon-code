from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils import themes_db, json


theme = Blueprint("theme", __name__, url_prefix="/theme")

limiter = Limiter(get_remote_address, app=theme, storage_uri="memory://")

@theme.route("/add", methods=["POST"])
@limiter.limit("5/30second")
def add_theme():
    return {
        "status": themes_db.addTheme(json["title"], json["description"], json["link"])
    }


@theme.route("/get-theme/<name>")
def get_theme(name):
    return themes_db.getTheme(name)


@theme.route("/get-themes")
def get_themes():
    return {"list": list(themes_db.getThemes())}
