from django.db import models

class Header(models.Model):
    tailwind = '<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>'
   
    def __str__(self):
        return self.name