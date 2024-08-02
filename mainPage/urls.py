from django.urls import path
from mainPage import views
from django.contrib.auth.views import LogoutView
from .views import CategoryDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('login', views.login_view, name='login'),
    path('newsletter', views.newletter, name='newsletter'),
    path('category', views.categoryBlade, name='cat'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('register-request', views.registerRequest, name='registerRequest'),


]
