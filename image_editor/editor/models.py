from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    """ Базовое изображение """
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/Images/files', blank=True)
    img_url = models.URLField(blank=True, default='')


    def get_absolute_url(self):
        return reverse('editor:resize', args=[self.id])