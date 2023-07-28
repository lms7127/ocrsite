from django.db import models
# Create your models here.
import uuid
import os

class Profile(models.Model):
    id= models.IntegerField(primary_key=True)
    
    def upload_to_func(instance, filename):
        file_name=uuid.uuid4().hex
        extension=os.path.splitext(filename)[-1].lower()
        return "/".join(
            [file_name, extension,]
        )
    
    image = models.ImageField(null=True, upload_to=upload_to_func)
    country=models.CharField(null=True,  max_length=50)
    def __str__(self):
        return self.title
    
