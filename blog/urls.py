from  . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('get_currency/', views.get_currency),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
]
