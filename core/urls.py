
from django.urls import path
from . import views

# O app_name ajuda a organizar as URLs e a referenciá-las nos templates
app_name = 'core'

urlpatterns = [
    # URL para a página inicial
    path('', views.homepage, name='homepage'),
]

