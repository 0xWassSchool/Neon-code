import os


appdata_path = os.path.join(os.environ["APPDATA"] + r"\neon_code")


def catch(func):
    def wrapper():
        try:
            return func()
        except Exception as e:
            return e

    return wrapper
