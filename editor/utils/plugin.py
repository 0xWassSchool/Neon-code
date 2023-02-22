class ImportPlugin:
    @staticmethod
    def load_plugin(file):
        return __import__(file).run()
