from django.urls import path
from . import views

urlpatterns = [
    path('404/',views.num),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('index/',views.index),
    path('details/',views.details),
]