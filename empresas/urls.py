from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresa_list, name='empresa_list'),
    path('empresa/<int:pk>/', views.empresa_detail, name='empresa_detail'),
    path('empresa/create/', views.empresa_create, name='empresa_create'),
    path('empresa/<int:pk>/update/', views.empresa_update, name='empresa_update'),
    path('empresa/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
