from omoika.elements import Markdown, Empty
from omoika import Plugin


class Whois(Plugin):
    version = "1.0.0"
    label = "Whois"
    category = "Web"
    color = "#F47C0099"
    elements = [
        Markdown(label="Raw"),
    ]
    icon = "world-question"
    author = "omoika"
    description = "whois.com allows you to trace the ownership and tenure of a domain name or an IP address"
