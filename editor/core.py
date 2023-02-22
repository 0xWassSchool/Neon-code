from editor.utils import read_file, appdata_path


get_json_content = read_file(appdata_path + r"\config\standard.json")

menu_bar_style = """
QMenuBar {
    color: white;
}
QMenuBar::item:selected {    
    background-color: #3A3731;
}

QMenu {
    color: white;
}
QMenu::item {
    color: white;
}
QMenu::item:selected { 
    background-color: #4B4740;
    color: white;
}"""
