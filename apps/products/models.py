from django.db import models

class Product(models.Model):
    CURRENCY_CHOICES = [
        ("$", "Dolar"),
        ("₺", "Türk Lirası"),
        ("€", "Euro"),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="$")

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}"
    
