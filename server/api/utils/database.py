from pymongo import MongoClient


client = MongoClient()
db = client["neon_database"]


class PlugIn:
    collection = db["plguin"]

    def addPlugin(self, title: str, description: str, link: str):
        """
        title: The title of your plugin
        description: The function of your plugin
        link: The link of your plugin
        """
        try:
            self.collection.insert_one(
                {"title": title, "description": description, "link": link}
            )
            return 1
        except:
            return 0

    def getPlugin(self, title: str):
        return self.collection.find_one({"title": title}, {"_id": 0})

    def getPlugins(self):
        try:
            for plugin in self.collection.find():
                yield plugin
        except:
            return 0


class THemes:
    collection = db["themes"]

    def addTheme(self, title: str, description: str, link: str):
        """
        title: The title of your theme
        description: The function of your theme
        link: The link of your plugin
        """
        try:
            self.collection.insert_one(
                {"title": title, "description": description, "link": link}
            )
            return 1
        except:
            return 0

    def getTheme(self, title):
        return self.collection.find_one({"title": title}, {"_id": 0})

    def getThemes(self):
        try:
            for plugin in self.collection.find():
                yield plugin
        except:
            return 0
