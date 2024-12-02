from .views import signUp,signIn,signOut
from django.urls import path

urlpatterns = [
    path('signUp/', signUp,name="signUp"),
    path('signIn/', signIn,name="signIn"),
    path('signOut/',signOut, name='signOut'),
]
