from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    # isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

