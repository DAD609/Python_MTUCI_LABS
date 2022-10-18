from site import venv
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('articles/' ,  views.archive, name='articles'),
    path ('article/<int:pk>/', views.archive, name='article'),
    path ('post/new/', views.create_post, name="create_post" ),
    path('user/register/', views.create_user, name="register"),
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),

]
