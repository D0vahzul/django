from django.contrib import admin
from .models import Blog
from django.utils.text import slugify

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            base_slug = slugify(obj.name)
            slug = base_slug
            num = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            obj.slug = slug
        super().save_model(request, obj, form, change)
