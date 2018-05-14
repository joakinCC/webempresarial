from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="entradas"),
    path('category/<int:category_id>/', views.category, name="category"),
]