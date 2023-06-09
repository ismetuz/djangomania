from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User



class TodoCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse( 
        "todo:category_view", 
        kwargs={"category_slug": self.slug}
        )
    
class TodoTag(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
        "todo:tag_view", 
        kwargs={"tag_slug": self.slug}
        )

class Todo(models.Model):
    # category = models.ForeignKey(Category, on_delete = models.CASCADE) #bunu kullanmıyoruz çünkü CASCADE yapınca
    #Category silindiğinde tüm ilişkili todolar da silinir..
    tag = models.ManyToManyField(TodoTag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TodoCategory,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
        "todo:todo_detail_view", 
        kwargs={"category_slug": self.category.slug,
                "id": self.pk,
                }
        )

    
    
