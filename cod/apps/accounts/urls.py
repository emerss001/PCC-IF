from django.urls import path
from . import views
from .classes import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView)

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login, name="login"),
    path('registrar/', views.registrar, name="registrar"),
    path('logout/', views.logout, name="logout"),

    path('reset/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset/password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


