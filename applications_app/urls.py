from django.urls import path, include
from rest_framework import routers
from .views import WriterInfoView, LoginView, CustomAuthToken, ApplicationNoList, ApplicationYesList#, RegistrUser
from . import serializers
from .views import UserLoginView, LoginView#RegisterPage,
from django.contrib.auth.views import LogoutView
from dj_rest_auth.views import LoginView, LogoutView as Logout


router = routers.DefaultRouter()
#router.register('api/login', CustomAuthToken.as_view(), 'login_user')
#router.register('api/registr', RegistrUser, 'register_user')
router.register('api/writer', WriterInfoView, 'write_info') #Основоной url для запси заявок через апи


#/api-auth/login/
urlpatterns = [
    #path('api/logout', Logout.as_view()),
    #path('api/login/', LoginView.as_view()),
    # User login endpoints
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
#    path("signup/", RegisterPage.as_view(), name="signup"),
    path("list_processed/", ApplicationYesList.as_view(), name="list_done"), # Просмотр списка обработанных заявок и их комментирование
    path("list_not_processed/", ApplicationNoList.as_view(), name="list"), # Просмотр списка не обработанных заявок и их комментирование
    path('', include(router.urls)),

    #path('registr/', RegistrUserView.as_view(), name='registr'),
    #path('login/', LoginView.as_view()),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]