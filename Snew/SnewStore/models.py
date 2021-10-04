from django.db import models
from django.contrib.auth.models import User
# Create your models here.

category = ((0,'Chính trị xã hội'),(1,'Đời sông'),(2,'Thể Thao'),(3,'Sức khỏe'),(4,'Khoa học'),(5,'Du lịch'))

class ProductDev(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    content = models.TextField()
    keyword = models.TextField()
    description = models.TextField()
    summary = models.TextField()
    category = models.SmallIntegerField(choices=category)
    def __str__(self):
        return self.title