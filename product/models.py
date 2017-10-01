from django.db import models

# Create your models here.

class Principle(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256,blank=True, null=True)
    contact_no = models.CharField(max_length=256)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory)
    principal = models.ForeignKey(Principle)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=45)
    weight = models.CharField(max_length=45)
    mop = models.CharField(max_length=45)
    pouch = models.IntegerField(blank=True,null=True)
    current_price_activated_on = models.DateField(blank=True, null=True)
    distributor_price = models.FloatField(blank=True, null=True)
    sell_price = models.FloatField(default=0.0)
    vat_manufacturer = models.FloatField(blank=True, null=True)
    vat_distributor = models.FloatField(blank=True, null=True)
    product_image = models.ImageField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " " + self.code

class ProductSell(models.Model):
    product = models.ForeignKey(Product)
    amount = models.IntegerField()
    sell_date = models.DateField()

    def __str__(self):
        return str(self.product) + ' ' + str(self.amount)
