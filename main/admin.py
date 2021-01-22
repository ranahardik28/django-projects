from django.contrib import admin
from .models import Blog_data, Views, Likes

# Register your models here.


class blogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views', 'likes', 'pub_date')


admin.site.register(Blog_data, blogAdmin)
admin.site.register(Views)
admin.site.register(Likes)
