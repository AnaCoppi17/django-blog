from django.db import models

# Create your models here.
class Post(models.Model):
    body_text = models.TextField('Texto principal')
    pub_date = models.DateTimeField('Data publicação', auto_now = True)