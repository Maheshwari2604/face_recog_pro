from django.db import models

# Create your models here.
class Users(models.Model):
    #name = models.CharField(max_length=100,null=False,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    user_img = models.ImageField(upload_to='user_images/',null=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

