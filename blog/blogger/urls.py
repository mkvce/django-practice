from django.urls import path
from blogger import views

app_name = 'blogger'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
