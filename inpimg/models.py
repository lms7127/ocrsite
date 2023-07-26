from django.db import models
# Create your models here.


class Profile(models.Model):
    id= models.IntegerField(primary_key=True)
    image = models.ImageField(null=True, upload_to='images/')
    country=models.CharField(null=True,  max_length=50)
    def __str__(self):
        return self.title
    
