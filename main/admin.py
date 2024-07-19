from django.contrib import admin
from .models import User, Category, Savollar, Javoblar
from django.contrib.auth.admin import UserAdmin





admin.site.register(Category)
admin.site.register(Savollar)
admin.site.register(Javoblar)
admin.site.register(User, UserAdmin)