from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imageURL= models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    
    