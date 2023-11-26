from django.urls import path
from . import views
from .views import MemberRegister

urlpatterns = [
    path('register/', MemberRegister.as_view(), name='register_form')
]

