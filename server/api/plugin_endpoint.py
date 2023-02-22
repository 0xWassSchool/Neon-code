from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils import plugin_db, json


plugin = Blueprint("plugin", __name__, url_prefix="/plugin")

limiter = Limiter(get_remote_address, app=plugin, storage_uri="memory://")


@plugin.route("/add", methods=["POST"])
@limiter.limit("5/30second")
def add_plugin():
    return {
        "status": plugin_db.addPlugin(json["title"], json["description"], json["link"])
    }


@plugin.route("/get-plguin/<name>")
def get_plugin(name):
    return plugin_db.getPlugin(name)


@plugin.route("/get-plguins")
def get_plugins():
    return {"list": list(plugin_db.getPlugins())}
