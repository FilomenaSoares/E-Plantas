from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, ProfileDetailView, ProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('perfil/editar/', ProfileUpdateView.as_view(), name='profile_update'),
    path('perfil/<str:username>/', ProfileDetailView.as_view(), name='profile'),
]