from django.urls import path

from . import views

urlpatterns = [
    path('<str:pk>/<str:status>', views.plansStatus, name='plansStatus'),
    path('<str:pk>/', views.plansDetail, name='plansDetail'),
    path('', views.index, name='index'),
]