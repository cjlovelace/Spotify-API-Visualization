import eel
from random import randint

eel.init("static_web_folder")


@eel.expose
def random_python():
    print("Random function running")
    return randint(1, 100)


eel.start("index.html")
