from django.contrib import admin
from .models import BlogPost
# Register your models here.
@admin.register(BlogPost)
class AdminBlogPost(admin.ModelAdmin):
    list_display = ['id','title','author']
