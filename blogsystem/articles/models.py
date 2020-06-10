from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    #date = models.DateTimeField('date published')
    date = models.DateTimeField(auto_now_add=True)
    thum= models.ImageField(default="default.png", blank= True)

    #thumnail
    #author
    def __str__(self):
        return self.title
        #return '{} {}'.format(self.title, self.body)
    # def datepublished(self):
    #     return self.date == timezone.now() - datetime.timedelta(days=1)
    #     #return self.date >= timezone.now() - datetime.timedelta(days =1)

    def snippit(self):
        return self.body[:50] + ' .... read more '


