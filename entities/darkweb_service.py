import omoika
from omoika.elements import TextInput


class DarkwebService(omoika.Plugin):
    version = "1.0.0"
    label = "Darkweb Service"
    category = "Web"
    color = "#6B728099"
    icon = "storm"
    author = "omoika"
    description = "Represent a darkweb/onion service reference."

    elements = [
        TextInput(label="Service Name", icon="ghost"),
        TextInput(label="Onion URL", icon="link"),
    ]
