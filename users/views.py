from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserCreationForm, ProfileUpdateForm
from blog.models import Post

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:homepage')

# --- NOVAS VIEWS PARA O PERFIL ---
class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile_user'
    slug_field = 'username' # Usa o username para buscar o usuário
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        # Pega os posts publicados e salvos pelo usuário do perfil
        context['user_posts'] = Post.objects.filter(author=user, status='PUBLISHED')
        context['saved_posts'] = user.saved_posts.all()
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'

    def get_object(self):
        # Garante que o usuário só pode editar o seu próprio perfil
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'username': self.request.user.username})
