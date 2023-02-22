import json

"""
    emplate structure:
    "version": "1.0.0",
    "ui": {
        "text-color": "white",
        "background": "#2A2824",
        "font-size": 12,
        "font": "Arial",
    },
}
"""
template = {
    "version": "1.0.0",
    "ui": {
        "text-color": "white",
        "background": "#2A2824",
        "font-size": 12,
        "font": "Arial",
    },
}


def read_file(file):
    return json.loads(open(file, "r").read())
