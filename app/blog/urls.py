from django.urls import path,include

from . import views
app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/',views.profile,name="profile"),
    path('register/',views.register, name="register"),
    path('shoes/',views.list_shoes, name="list_shoes"),
    path('shoes/add',views.add_shoes, name="add_shoes")
]


