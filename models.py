from django.db import models
from django.utils.html import format_html


# Create your models here.

class category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
         return format_html('<img src = "/media/{} " style= "width:100px;height:100px;border-radius:50%  "/> '.format(self.image))

    def __str__(self):
        return self.title



class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content =models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def image_tag(self):
         return format_html('<img src = "/media/{} " style= "width:100px;height:100px;border-radius:50%  "/> '.format(self.image))

    def __str__(self):
        return self.title


