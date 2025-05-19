from django.utils.crypto import get_random_string
from django.utils.text import slugify

def unique_slugify(instance, text, restricted_slugs=None):
    if restricted_slugs is None:
        restricted_slugs = []

    base_slug = slugify(text)
    slug = base_slug

    model = instance.__class__
    reserved = restricted_slugs + ['add', 'edit', 'delete', 'all', 'new']

    # Yasaklı slug'lara karşı önlem
    if slug in reserved:
        slug = f"{slug}-{get_random_string(4)}"

    # Aynı slug varsa benzersizleştir
    while model.objects.exclude(pk=instance.pk).filter(slug=slug).exists():
        slug = f"{base_slug}-{get_random_string(4)}"

    return slug
