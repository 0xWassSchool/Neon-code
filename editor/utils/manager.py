import os

from abc import ABCMeta, abstractmethod
from editor.utils._intert_core import catch, appdata_path


functions = {}


def instances(name):
    def wrapper(func):
        functions[name] = func

        return func

    return wrapper


class IAddons(metaclass=ABCMeta):
    @abstractmethod
    def save(self, file, content):
        pass

    @abstractmethod
    def delete(self, file):
        pass


@instances("plugin")
class Plugin(IAddons):
    @catch
    def save(self, file, content):
        with open(appdata_path + f"\plugins\installed\{file}.py", "w") as file:
            file.write(content)
            file.close()
        return 0

    @catch
    def delete(self, filename):
        os.remove(appdata_path + f"\plugins\installed\{filename}.py")
        return 0


@instances("theme")
class Theme(IAddons):
    @catch
    def save(self, file, content):
        with open(appdata_path + f"\themes\installed\{file}.py", "w") as file:
            file.write(content)
            file.close()
        return 0

    @catch
    def delete(self, file):
        os.remove(appdata_path + f"\themes\installed\{file}.py")
        return 0


class Factory:
    @staticmethod
    def addons(class_, file, content=None):
        if class_ == "plugin-save":
            return functions["plugin"]().save(file=file, content=content)
        elif class_ == "plugin-delete":
            return functions["plugin"]().delete(file=file)
        elif class_ == "theme-save":
            return functions["theme"]().save(file=file, content=content)
        elif class_ == "theme-delete":
            return functions["theme"]().delete(file=file)
        else:
            return Exception("Action not found")
