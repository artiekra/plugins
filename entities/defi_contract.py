import omoika
from omoika.elements import TextInput


class DeFiContract(omoika.Plugin):
    version = "1.0.0"
    label = "DeFi Contract"
    category = ["Cryptocurrency", "Finance"]
    color = "#8B5CF699"
    icon = "currency-ethereum"
    author = "omoika"
    description = "Represent a smart contract (address/network)."

    elements = [
        TextInput(label="Contract Address", icon="hash"),
        TextInput(label="Network", icon="network"),
    ]
