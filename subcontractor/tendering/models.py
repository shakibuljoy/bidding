from django.db import models

class ComparetiveStatement(models.Model):
    title = models.CharField(max_length=200)
    project_name = models.CharField(max_length=50)
    location  = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    unit = models.CharField(max_length=10)
    apprx_qty = models.PositiveIntegerField(blank=True, null=True)
    cs = models.ForeignKey(ComparetiveStatement, on_delete=models.CASCADE)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class ItemPrice(models.Models):
    price = models.PositiveIntegerField(default=0)
    cs = models.ForeignKey(ComparetiveStatement, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)