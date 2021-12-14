from django.db import models

class Table(models.Model):
    state = models.CharField(max_length=100)


    def __str__(self):
        return self.state


class Product(models.Model):
    name = models.CharField(max_length=200)
    imported = models.CharField(max_length=100, verbose_name='Imported From')
    number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
