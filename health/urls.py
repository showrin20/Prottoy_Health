from .views import checkUp,heartDisease,resultView
from django.urls import path

urlpatterns = [
    path('checkup/', checkUp,name="checkup"),
    path('heartDisease/',heartDisease,name='heartDisease'),
    path('result/',resultView, name="result")
]
