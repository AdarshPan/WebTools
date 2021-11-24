from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Members)
admin.site.register(models.Scores)
admin.site.register(models.Post)
admin.site.register(models.post_comments)
admin.site.register(models.MusicCreate)