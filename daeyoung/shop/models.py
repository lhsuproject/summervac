from django.db import models
# Create your models here.

#게시물 모델
class Item(models.Model):
    image = models.ImageField(upload_to = 'media', blank=True, null=True)
    title = models.CharField(max_length=200)
    money = models.IntegerField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    

    
