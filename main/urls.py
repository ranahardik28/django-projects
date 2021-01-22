from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [

    path('', views.go_main, name="go_main"),
    path('index/<str:cat>/', views.index, name="index"),
    path('detail/<int:blog_id>/', views.detail_page, name="detail_page"),
    path('test', views.test)

]
