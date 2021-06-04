"""First_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Mandy import views
from blog import views2

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('Mandy.urls'),name="main"),
    # path('services/',include('Mandy.urls'),name="services"),
    # path('contact/',include('Mandy.urls'),name="contact"),
    # path('blog/',include('Mandy.urls'),name="blog"),
    # path('', include('blog.urls'))
    path('',views.main,name="main"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="contact"),
    path('why_us/',views.why_us,name="contact"),
    path('vision/',views.vision,name="contact"),
    path('mission/',views.mission,name="contact"),
    path('Career/',views.career,name="contact"),
    path('blog/',views2.PostList.as_view(),name="blog"),
    # path('', include('blog.urls')),
    path('blog/<slug:slug>/', views2.PostDetail.as_view(), name='post_detail'),
    path('.well-known/brave-rewards-verification.txt', TemplateView.as_view(template_name="brave-rewards-verification.txt", content_type="text/plain"),)
]

