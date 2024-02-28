from django.contrib import admin
from main.models import BlogpostModel, CategoryModel, AuthorModel

admin.site.register(BlogpostModel)
admin.site.register(AuthorModel)
admin.site.register(CategoryModel)

