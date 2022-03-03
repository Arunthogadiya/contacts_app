from django.contrib import admin
from django.urls import path, include
from users import views as users_view
from django.contrib.auth import views as auth
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('login/', users_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='users/login.html'), name ='logout'),
    path('register/', users_view.register, name ='register'),
 
]