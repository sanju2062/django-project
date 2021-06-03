from . import views2
from django.urls import path

urlpatterns = [
    path('', views2.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views2.PostDetail.as_view(), name='post_detail'),
]