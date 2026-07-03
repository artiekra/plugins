import omoika
from omoika.elements import TextInput


class TrainStation(omoika.Plugin):
    version = "1.0.0"
    label = "Train Station"
    category = ["Locations", "Transportation"]
    color = "#A78BFA99"
    icon = "train"
    author = "omoika"
    description = "Represent a train station."

    elements = [
        TextInput(label="Name", icon="building-rail"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

