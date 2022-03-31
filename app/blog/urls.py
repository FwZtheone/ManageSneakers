from django.urls import path,include

from . import views
app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('profile/',views.profile,name="profile"),
    path('register/',views.register, name="register")
]


