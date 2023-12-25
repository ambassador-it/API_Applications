from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .forms import  CommentForm #CustomUserCreationForm,
from .serializers import  WriterSerializer#, UserRegistrSerializer,

# Подключаем статус
from rest_framework import status
# Подключаем компонент для ответа
from rest_framework.response import Response
# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView
# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, get_user_model, authenticate

from .models import Аpplication#, CustomUser

# Подключаем UserRegistrSerializer
#from .serializers import UserRegistrSerializer

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'





class UserLoginView(LoginView):
    template_name = "registration/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("list")


# class RegisterPage(FormView):
#     template_name = "signup.html"
#     form_class = CustomUserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy("login")
#
#     def form_valid(self, form):
#         """
#         Redirects the user ones the signup form is submitted. We make sure that user is logged in.
#         Triggered ones the POST-request to a signup sent.
#         """
#         user = form.save()
#         if user:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)
#
#     def get(self, *args, **kwargs):
#         """To redirect the authenticated user to the tasks list from the signup page."""
#         if self.request.user.is_authenticated:
#             return redirect("login")
#         return super(RegisterPage, self).get(*args, **kwargs)
#


class ApplicationNoList(LoginRequiredMixin, ListView):
    """Observe all over the task list and the options to add some new or search from list."""
    model = Аpplication
    template_name = 'new_application.html'
    context_object_name = "application_list"
    #fields = '__all__'
    #success_url = reverse_lazy("list")
    #form_class = CommentForm

    def get_context_data(self, **kwargs):
        form = CommentForm()
        #print(self.request.GET.get('comment_area'))
        #print(self.request.POST['comment_area'])
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["object_list"].filter(status=0)
        #context["tasks"].
        #context = super(ApplicationList, self).get_context_data()
        #context['phone'] = CustomUser.objects.get(username=self.request.user).phone_number
        context['form'] = form

        # print(form.cleaned_data)
        return context

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST, instance=Аpplication.objects.filter(pk=request.POST.get('id')).first())
        if form.is_valid():

            form.save()
            return super(ApplicationNoList, self).get(request, *args, **kwargs)
        else:
            return super(ApplicationNoList, self).get(*args, **kwargs)


class ApplicationYesList(LoginRequiredMixin, ListView):
    """Observe all over the task list and the options to add some new or search from list."""
    model = Аpplication
    template_name = 'yes_application.html'
    context_object_name = "application_list"
    #fields = '__all__'
    #success_url = reverse_lazy("list_done")
    #form_class = CommentForm

    def get_context_data(self, **kwargs):
        form = CommentForm()
        #print(self.request.GET.get('comment_area'))
        #print(self.request.POST['comment_area'])
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["object_list"].filter(status=1)
        #context = super(ApplicationList, self).get_context_data()
        #context['phone'] = CustomUser.objects.get(username=self.request.user).phone_number
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST, instance=Аpplication.objects.filter(pk=request.POST.get('id')).first())
        #form.status = request.POST['status']
        if form.is_valid():

            if form.cleaned_data['comments'] == '':

                form.save()
            form.save()
            return super(ApplicationYesList, self).get(request, *args, **kwargs)
        else:
            return super(ApplicationYesList, self).get(*args, **kwargs)


    # Создаём класс RegistrUserView
# class RegistrUser(CreateModelMixin, GenericViewSet):
#     model = get_user_model()
#     # Добавляем в queryset
#     queryset = CustomUser.objects.all()
#     # Добавляем serializer UserRegistrSerializer
    #serializer_class = UserRegistrSerializer
    # Добавляем права доступа
    #permission_classes = [permissions.AllowAny]

    # Создаём метод для создания нового пользователя
    # def post(self, request, *args, **kwargs):
    #     # Добавляем UserRegistrSerializer
    #     serializer = UserRegistrSerializer(data=request.data)
    #     # Создаём список data
    #     data = {}
    #     # Проверка данных на валидность
    #     if serializer.is_valid():
    #         # Сохраняем нового пользователя
    #         serializer.save()
    #         # Добавляем в список значение ответа True
    #         data['response'] = True
    #         # Возвращаем что всё в порядке
    #         return Response(data, status=status.HTTP_200_OK)
    #     else:  # Иначе
    #         # Присваиваем data ошибку
    #         data = serializer.errors
    #         # Возвращаем ошибку
    #         return Response(data)
    # def post(self, request):
    #
    #     serializer_for_writing = self.serializer_class(data=request.data)
    #     serializer_for_writing.is_valid(raise_exception=True)
    #     serializer_for_writing.save()
    #     return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)




from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response

from . import serializers

# class LoginView(views.APIView):
#     def post(self, request, format=None):
#         data = request.data
#
#         username = data.get('username', None)
#         password = data.get('password', None)
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#
#                 return Response(status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class WriterInfoView(ModelViewSet):
    queryset = Аpplication.objects.all()
    serializer_class = WriterSerializer
    model = Аpplication
    http_method_names = ['post']

    def post(self, request):

        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)

