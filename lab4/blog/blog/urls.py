from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('articles/' ,  views.archive, name='articles'),
    path ('article/<int:pk>/', views.archive, name='article'),

]
