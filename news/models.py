from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Category(BaseModel):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
    def __str__(self):
        return self.name

class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News List")
    
    def __str__(self):
        return self.title
