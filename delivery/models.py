from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images", blank=True)
    category = models.ManyToManyField(Category)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





