from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='books')  # Một sách có nhiều thể loại
    publisher = models.CharField(max_length=100, default='Unknown')
    publication_year = models.IntegerField(default=2023)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Ảnh sách (có thể null)

    def __str__(self):
        return self.title
