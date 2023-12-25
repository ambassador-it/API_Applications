# Подключаем класс для работы со сериалайзер
from rest_framework import serializers
# Подключаем модель user
from .models import Аpplication# CustomUser,


# class UserRegistrSerializer(serializers.ModelSerializer):
#     # Поле для повторения пароля
#     password2 = serializers.CharField()
#
#     # Настройка полей
#     class Meta:
#         # Поля модели которые будем использовать
#         model = CustomUser
#         # Назначаем поля которые будем использовать
#         fields = ['username', 'password', 'password2']#, 'phone_number']
#
#     # Метод для сохранения нового пользователя
#     def save(self, *args, **kwargs):
#         # Создаём объект класса User
#         user = CustomUser(
#             #email=self.validated_data['email'],  # Назначаем Email
#             username=self.validated_data['username'],
#             #phone_number=self.validated_data['phone_number']# Назначаем Логин
#         )
#         # Проверяем на валидность пароль
#         password = self.validated_data['password']
#         # Проверяем на валидность повторный пароль
#         password2 = self.validated_data['password2']
#         # Проверяем совпадают ли пароли
#         if password != password2:
#             # Если нет, то выводим ошибку
#             raise serializers.ValidationError({password: "Пароль не совпадает"})
#         # Сохраняем пароль
#         user.set_password(password)
#         # Сохраняем пользователя
#         user.save()
#         # Возвращаем нового пользователя
#         return user

from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

# class LoginSerializer(serializers.Serializer):
#     """
#     This serializer defines two fields for authentication:
#       * username
#       * password.
#     It will try to authenticate the user with when validated.
#     """
#     username = serializers.CharField(
#         label="Username",
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         # This will be used when the DRF browsable API is enabled
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True
#     )
#
#     def validate(self, attrs):
#         # Take username and password from request
#         username = attrs.get('username')
#         password = attrs.get('password')
#
#         if username and password:
#             # Try to authenticate the user using Django auth framework.
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password)
#             if not user:
#                 # If we don't have a regular user, raise a ValidationError
#                 msg = 'Access denied: wrong username or password.'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Both "username" and "password" are required.'
#             raise serializers.ValidationError(msg, code='authorization')
#         # We have a valid user, put it in the serializer's validated_data.
#         # It will be used in the view.
#         attrs['user'] = user
#         return attrs


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        # Поля модели которые будем использовать
        model = Аpplication
        # Назначаем поля которые будем использовать
        fields = ['phone_number', 'description']


    def create(self, validated_data):
        return Аpplication.objects.create(**validated_data) #user=self.context['request'].user,



UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password', 'username', 'first_name', 'last_name',)