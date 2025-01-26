from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title