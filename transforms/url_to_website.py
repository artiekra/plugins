import re
from urllib.parse import urlparse

from omoika import Registry, transform
from omoika.errors import PluginError

# looks for anything after http(s):// or www. and grabs the main host
PATTERN = r"^(?:https?:\/\/)?(?:www\.)?([^\/\s?#:]+)"


@transform(target="url@1.0.0", label="To website", icon="world-www")
async def to_website(self, entity):
    website_entity = await Registry.get_entity("website")
    url = entity.url
    if not url:
        raise PluginError("Must specify URL to convert to website.")

    match = re.search(PATTERN, url.lower())
    domain = match.group(1) if match else ""
    return website_entity.create(domain=domain)
