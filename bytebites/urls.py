from django.urls import path
from bytebites import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about)
]
