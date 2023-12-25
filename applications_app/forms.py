from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Аpplication #CustomUser,


#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username',)# 'phone_number')
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username',)#, 'phone_number')


class CommentForm(forms.ModelForm):
    # parent_comment = forms.IntegerField(
    #     widget=forms.HiddenInput,
    #     required=False
    # )
    attrs = {'rows': '2', 'cols': '20'}

    class Meta:
        model = Аpplication
        fields = ('comments', 'status', 'date')
        #attrs = {'rows': '2', 'cols': '20'}
        widgets = {
            'date': forms.SelectDateWidget()
        }


class АpplicationForm(forms.Form):
    class Meta:
        model = Аpplication
        fields = ('user', 'description', 'status', 'created_at', 'phone_number')
