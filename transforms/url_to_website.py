from urllib.parse import urlparse
from omoika import transform, Registry


@transform(
    target="url@1.0.0",
    label="To website",
    icon="world-www"
)
async def to_website(self, entity):
    website_entity = await Registry.get_entity('website')
    domain = urlparse(entity.url).netloc
    return website_entity.create(domain=domain)
