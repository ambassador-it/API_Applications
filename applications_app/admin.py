from django.contrib import admin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin
from .models import Аpplication
#from .forms import  CommentForm, АpplicationForm #CustomUserCreationForm, CustomUserChangeForm,
#from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]# 'phone_number']
#
# admin.site.register(CustomUser, CustomUserAdmin)
# # Register your models here.


class CustomАpplicationAdmin(admin.ModelAdmin):

    list_display = ('short_description', 'status', 'created_at', 'phone_number')

    def short_description(self, obj):
        return obj.description[:25] + '...'
    short_description.short_description = 'Описание'



admin.site.register(Аpplication, CustomАpplicationAdmin)
