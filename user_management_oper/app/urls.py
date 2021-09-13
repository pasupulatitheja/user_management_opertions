from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('',TemplateView.as_view(template_name="login.html")),
    path('register/',TemplateView.as_view(template_name="badmin/register.html"),name='register'),
    path('save_user/',views.save_user_deatils,name="save_user"),
    # path('adminloginpage/',TemplateView.as_view(template_name="badmin/homepage.html"),name="adminloginpage" ),
    path('welcome_page/',views.showadminwelcome,name='welcome_page'),
]
