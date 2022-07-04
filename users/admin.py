from django.contrib import admin
from users.models import User_profile

# Register your models here.

# admin.site.register(User_profile)

@admin.register(User_profile)
class UserProfile(admin.ModelAdmin):
    list_display = ["user", "phone"]
    