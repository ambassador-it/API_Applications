from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator



# class CustomUser(AbstractUser):
#
#     # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, primary_key=True) # Validators should be a list
#     # # add additional fields in here
#
#     def __str__(self):
#         return self.username

class Аpplication(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Номер телефона')  # Validators should be a list
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(blank=True, null=True, verbose_name='Дата')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    STATUS = [(0, 'Не обработано'), (1, 'Обработано'),]
    status = models.BooleanField(max_length=32, choices=STATUS, default=0, verbose_name='Статус')
    #is_processed = models.BooleanField(default=False, null=True, blank=True),
    comments = models.TextField(max_length='100', blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return self.phone_number
