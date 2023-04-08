from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog),
    path('blog/<slug:slug>/', views.blogPost),
]
