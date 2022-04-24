from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('blog/', views.blog),
    path('blog/<int:pk>/', views.single_post_page)
]





