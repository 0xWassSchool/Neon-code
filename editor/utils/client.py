import requests


class HttpClient:
    base = ""

    def get_plugin(self, name, path="/get-plguin"):
        url = self.base + path + "/" + name
        return requests.get(url).content

    def get_theme(self, name, path="/get-theme"):
        url = self.base + path + "/" + name
        return requests.get(url).content

    def get_plugins(self, path="/get-plguins"):
        url = self.base + path
        return requests.get(url).json()["list"]

    def get_themes(self, path="/get-themes"):
        url = self.base + path
        return requests.get(url).json()["list"]
