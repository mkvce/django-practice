from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    num_of_articles = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    nick_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta():
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='related_articles')
    title = models.CharField(max_length=128)
    brief = models.CharField(max_length=256, blank=True)
    text = models.TextField(null=True)

    def save(self, *args, **kwargs):
        self.author.num_of_articles += 1
        self.author.save()
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.author.num_of_articles -= 1
        self.author.save()
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
