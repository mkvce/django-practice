from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name="سن")
    num_of_articles = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True, verbose_name="تصویر پروفایل")

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    nick_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
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
