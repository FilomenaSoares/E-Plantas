from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        COMMON = "COMMON", "Comum"
        CONTRIBUTOR = "CONTRIBUTOR", "Contribuidor"
        MODERATOR = "MODERATOR", "Moderador"

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.COMMON, verbose_name="Papel")
    
    # --- NOVOS CAMPOS PARA O PERFIL ---
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        default='profile_pics/default.jpg', 
        verbose_name="Foto de Perfil"
    )
    bio = models.TextField(blank=True, verbose_name="Biografia")

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})

