from django.db import models

# Create your models here.
class OrderForm(models.Model):
    AMOUNT_LEVEL =(
        ('0', 'zero'),
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three')
    )
    CONDOMINIOS = (
        ('ccm', 'cruz con mar'),
        ('miranda', 'miranda'),
        ('marea34', 'marea34')
    )
    name = models.CharField(max_length=50)
    condo = models.CharField(max_length=20, choices=CONDOMINIOS, default='ccm')
    amount = models.CharField(max_length=1, choices=AMOUNT_LEVEL)

    def name_is_lower(self):
        return str(self.name).islower()

