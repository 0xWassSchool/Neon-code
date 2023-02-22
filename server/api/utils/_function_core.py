from flask import request
from utils.database import *


plugin_db = PlugIn()
themes_db = THemes()


try:
    json = request.get_json()
except:
    pass
