from django.urls import path, include
from .views import CadastroView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cadastro/', CadastroView, name="cadastro"),
]