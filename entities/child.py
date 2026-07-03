import omoika
from omoika.elements import TextInput


class Child(omoika.Plugin):
    version = "1.0.0"
    label = "Child"
    category = "Identity"
    color = "#60A5FA99"
    icon = "baby-carriage"
    author = "omoika"
    description = "Represent a child (basic demographics)."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

