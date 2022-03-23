
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/', views.board_topics, name='board_topics'),
    path('admin/', admin.site.urls),
]
