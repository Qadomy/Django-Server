from django.urls import path

from boards import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
