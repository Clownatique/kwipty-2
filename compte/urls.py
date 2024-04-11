from django.urls import path
from . import views
from .views import SignUpView, CustomLoginView

urlpatterns = [
    path('', views.page_accueil, name='accueil'),
    path("inscription/", SignUpView.as_view(), name="inscription"),
    path('connexion/', CustomLoginView.as_view(), name='connexion'),
    path('dashboard/', views.menu_principal, name='menu'),
    path('dashboard/tuto/', views.menu_tuto, name='menu-tuto'),

]
