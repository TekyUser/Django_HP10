from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
