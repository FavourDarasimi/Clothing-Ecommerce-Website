from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

user = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")
    image = models.ImageField(upload_to="image/", blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=150, null=False, blank=False)
    details = models.TextField(max_length=500, null=False)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")
    new = models.BooleanField(default=True, help_text="0-default, 1-Hidden")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail")


class Comment(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("product_detail",kwargs={'pk': self.product.pk})


class Cart(models.Model):
    customer = models.ForeignKey(user, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse("product_detail")

    def __str__(self):
        return str(self.customer)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=1000000000000, decimal_places=2,null=True)
    quantity = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

    def get_absolute_url(self):
        return reverse("product_detail")



# Create your models here.
