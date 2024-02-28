from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    name = models.CharField(max_length=128)
    bio = models.CharField(max_length=128)
    email = models.EmailField()

    class Meta:
        verbose_name='Author'
        verbose_name_plural='Authors'

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class BlogpostModel(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blogpost")
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return self.title































    
    content = models.TextField()
    # author = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blogpost_images/')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE,null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    # TODO:
    # create author and category model
    # update temp with django temp
    # homepage, category, posts page using bootstrap

    


