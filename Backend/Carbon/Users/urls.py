
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register',views.Register,name="register"),
    path('login',views.Login,name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin_login',views.admin_login,name="admin login"),
    path('logout',views.Logout,name="logout")
]
