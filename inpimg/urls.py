from django.urls import path

from inpimg import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload),
    path('upload_create/',views.upload_create,name="upload_create"),
    
    
    ]