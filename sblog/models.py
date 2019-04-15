from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    categories = models.CharField(max_length=300)
    like_count = models.IntegerField(null=True)
    icon = models.FileField()
    post_date = models.DateField('posted Date')



    def __unicode__(self):
        return self.title
