from django.db import models

#Part 1: 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    #Method
    def product_info(self):
        return f"{self.name} costs ₱{self.price:g}"
    
    def __str__(self):
        return self.name