from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "user_class", "created")
    list_filter = ("name",)
    list_editable = ("name",)
    list_display_links = ("created",)
    

admin.site.register(User, UserAdmin)