from django.contrib import admin
from .models import category,post

# Register your models here.

class categoryadmin(admin.ModelAdmin):

    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)


class postadmin(admin.ModelAdmin):

    list_display = ('image_tag','post_id','title','content','url','cat')
    search_fields = ('title','post_id','url')
    list_filter =('cat',)

    class Media:
        js= ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)



admin.site.register(category,categoryadmin)
admin.site.register(post,postadmin)
