
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'



    def __str__(self):
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
