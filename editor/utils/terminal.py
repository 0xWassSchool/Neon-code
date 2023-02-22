import os
import sys
import json
import subprocess as process


from colorama import Fore
from editor.utils.manager import Factory
from editor.utils.client import HttpClient
from editor.utils.templates import template
from editor.utils.plugin import ImportPlugin
from editor.utils._intert_core import catch


commands = {}

manager = Factory()
http_client = HttpClient()
import_plugin = ImportPlugin()


def command(name):
    def wrapper(func):
        commands[name] = func
        return func

    return wrapper


@command("help")
def help():
    return """
    Separetor: ;

    Main commands:
    create: path
    run: interpeter path
    
    Addons:
    load-plugin: file
    install-plugin: file name
    delete-plugin: file
    
    install-theme: file name
    delete-theme: file
    
    Other commands:
    exec-git: command
    generate-template-json: None

    """


@catch
@command("create")
def create(path):
    open(os.getcwd() + "\\" + path.strip(), "w")

    return f"{path} created"


@catch
@command("run")
def run(interpreter, path):
    return process.getoutput(f"{interpreter} {path}")


@catch
@command("load-plugin")
def load_plugin(file):
    return import_plugin.load_plugin(file)


@catch
@command("install-plugin")
def install_plugin(file, name):
    return manager.addons("plugin-save", file, http_client.get_plugin(name))


@catch
@command("delete-plugin")
def delete_plugin(file):
    return manager.addons("plugin-delete", file)


@catch
@command("install-theme")
def install_theme(file, name):
    return manager.addons("theme-save", file, http_client.get_plugin(name))


@catch
@command("delete-them")
def delete_theme(file):
    return manager.addons("theme-delete", file)


@catch
@command("exec-git")
def exec_git(command):
    return process.getoutput(f"git {command}")


@catch
@command("generate-template-json")
def generate_json():
    return json.dumps(template)


class Terminal:
    @staticmethod
    def commands():
        while True:
            raw_command = input(Fore.BLUE + ">> " + Fore.RESET).split(";")

            if raw_command[0] == "help":
                print(help())

            # execution commands
            elif raw_command[0] == "create":
                print(commands["create"](raw_command[1]))
            elif raw_command[0] == "run":
                print(commands["run"])(raw_command[1], raw_command[2])
            # plugins and themes management
            elif raw_command[0] == "load-plugin":
                print(commands["load-plugin"])(raw_command[1])
            elif raw_command[0] == "install-plugin":
                print(commands["install-plugin"])(raw_command[1], raw_command[2])
            elif raw_command[0] == "delete-plugin":
                print(commands["delete-plugin"])(raw_command[1])
            elif raw_command[0] == "install-theme":
                print(commands["install-plugin"])(raw_command[1], raw_command[2])
            elif raw_command[0] == "delete-theme":
                print(commands["delete-plugin"])(raw_command[1])
            # git execution
            elif raw_command[0] == "exec-git":
                print(commands["exec-git"])(raw_command[1])
            # generate template -> json
            elif raw_command[0] == "generate-template-json":
                print(commands["generate-template-json"])()
            # standard commands
            elif raw_command[0] == "cls":
                os.system("cls")
            elif raw_command[0] == "exit":
                sys.exit()

            else:
                print(f"Command not found: {raw_command}")
