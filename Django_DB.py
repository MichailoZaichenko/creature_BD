from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    picture = models.ImageField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()
    pickup_point = models.ForeignKey('PickupPoint', on_delete=models.CASCADE)
    date_time = models.IntegerField()
    type_pay = models.TextField()
    status = models.TextField()
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return str(self.pk)


class OrderProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order} - {self.product}'


class User(models.Model):
    id_telegram = models.IntegerField(primary_key=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, default=1)
    name = models.TextField()
    last_name = models.TextField()
    picture = models.ImageField()
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField()

    def __str__(self):
        return self.name


class PickupPoint(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    coordinates = models.TextField()

    def __str__(self):
        return self.name