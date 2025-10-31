from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('posts/<int:pk>', views.PostDetailView.as_view(),name='post-deatil ')
    
]
