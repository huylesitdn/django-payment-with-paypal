from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/<str:status>', views.plansStatus, name='plansStatus'),
    path('<int:pk>/', views.plansDetail, name='plansDetail'),
    path('', views.index, name='index'),
]