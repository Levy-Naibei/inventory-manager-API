from django.db import models


# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=20, help_text='stock keeping unit')
    barcode = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.TextField()
    unit_cost = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=12, blank=True, null=True)
    quantity = models.FloatField()
    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of product"""
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Family(models.Model):
    reference = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()
    unit = models.CharField(max_length=10, blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Family."""
        return reverse('family_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Location(models.Model):
    reference = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Location. """
        return reverse('location_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Transaction(models.Model):
    sku = models.CharField(max_length=13)
    barcode = models.CharField(max_length=13)
    comment = models.TextField()
    unitCost = models.FloatField(blank=True, null=True)
    quantity = models.FloatField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    REASONS = (
        ('ns', 'New Stock'),
        ('ur', 'Usable Return'),
        ('nr', 'Unusable Return'),
    )

    reason = models.CharField(max_length=2, choices=REASONS, blank=True, default='ns')

    def get_absolute_url(self):
        """Returns the url to access a particular instance of transaction."""
        return reverse('transaction_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Transaction :  %d' % self.id
