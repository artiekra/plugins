import omoika
from omoika.elements import TextInput


class FaviconHash(omoika.Plugin):
    version = "1.0.0"
    label = "Favicon Hash"
    category = "Web"
    color = "#EC489999"
    icon = "favicon"
    author = "omoika"
    description = "Represent an HTTP favicon hash (e.g., for Shodan/Censys)."

    elements = [
        TextInput(label="MD5 Hash", icon="hash"),
        TextInput(label="URL", icon="link"),
    ]

