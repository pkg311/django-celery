
from django.urls import path
from . import views

urlpatterns = (

    path('', views.home, name='home_page'),
    path('Home', views.home, name='Home'),
    path('About', views.about, name='About'),
    path('Contact', views.contact, name='Contact'),
    path('result/<str:task_id>', views.Check_result, name='check_result'),
)