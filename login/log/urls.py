from . import views
from django.urls import path
urlpatterns=[
    path('hello',views.demo,name='name'),
    path('login',views.login,name='login')
]