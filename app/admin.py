from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title',"id","slug","author")
    prepopulated_fields= {"slug":("title",),}

admin.site.register(models.Category)

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username','id','email', 'first_name', 'last_name')
    readonly_fields = ('id',)

admin.site.register(User, CustomUserAdmin)