from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    info = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="user/")
    
    
    


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    
    
    
    
    
class Savollar(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="savollar")
    question = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="savollar")
    def __str__(self):
        return self.question


    @property
    def javoblar(self):
        return self.javob.count()
    
    
    @property
    def hamma_javoblar(self):
        return self.javob.all()

class Javoblar(models.Model):
    togri = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    savol = models.ForeignKey(Savollar, on_delete=models.CASCADE, related_name="javob")
    javob = models.CharField(max_length=200)
    
    def __str__(self):
        return self.javob
    
