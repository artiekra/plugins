import omoika
from omoika.elements import TextInput


class OnionService(omoika.Plugin):
    version = "1.0.0"
    label = "Onion Service"
    category = "Web"
    color = "#4B556399"
    icon = "storm"
    author = "omoika"
    description = "Represent a Tor hidden service (v3)."

    elements = [
        TextInput(label="Onion URL", icon="link"),
        TextInput(label="Category", icon="tag"),
    ]
