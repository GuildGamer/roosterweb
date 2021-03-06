from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

CATEGORY_CHOICES = (
    ('MF', 'Men\'s Fashion'),
    ('WF', 'Women\'s Fashion'),
    ('CJ', 'Clothing and Jewelry'),
    ('FO', 'Food'),
    ('WD', 'Web & Mobile Development'),
    ('ED', 'Electronics and Devices'),
    ('AS', 'Art and Stationary')
)

LABEL_CHOICES = (
    ('N', 'New'),
    ('B', 'Bestseller'),
    ('S', 'Special Deal')
)

class Vendor(models.Model):
    seller = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    shop_name = models.CharField(blank=True, null=True, max_length=20)
    phone_number = models.CharField(blank=True, null=True, max_length=20)
    city = models.CharField(blank=True, null=True, max_length=20) #remember to make this such t password = models.CharField(blank=True, null=True, max_length=20)
    store_category = models.CharField(blank=True, null=True, max_length=20) #remember to make this such that it gives you a list to choose from

    def __str__(self):
        return self.shop_name

    


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    image_1 = models.ImageField(blank=True, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('base_app:product', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
       return reverse('base_app:add-to-cart', kwargs={'slug': self.slug})
    
    def get_remove_from_cart_url(self):
       return reverse('base_app:remove-from-cart', kwargs={'slug': self.slug})

    def get_remove_single_item_from_cart_url(self):
       return reverse('base_app:remove-single-item-from-cart', kwargs={'slug': self.slug})
    
    if discount_price:
        if type(discount_price) == 'NoneType':
            discount_price = 0.0
        
        def get_discount_percentage(self):
                percentage = int(((self.price - self.discount_price)/self.price)*100)
                return percentage

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    rating = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    review = models.CharField(max_length=250)

   

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) 

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total_item_price(self):
        return self.quantity*self.item.price

    def get_total_discount_item_price(self):
        return self.quantity*self.item.discount_price
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    creation_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=20)
    order_notes = models.CharField(max_length=200)

    def __str__(self):

        return self.user.username

