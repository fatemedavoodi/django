from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Course(models.Model):
    image = models.ImageField(upload_to='course',default='default.png')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.title