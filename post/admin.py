from django.contrib import admin
from post.models import Posts

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "published_date")


admin.site.register(Posts, PostAdmin)
