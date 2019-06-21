from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishes_index, name='wishes_index'),
    path('create/', views.WishCreate.as_view(), name='wishes_create'),
    path('<int:wish_id>/delete/', views.wishes_delete, name='wishes_delete'),
]
