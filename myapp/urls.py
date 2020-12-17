from django.urls import path

from myapp.views import AppleView

urlpatterns = [
    path('', AppleView.as_view()),
]
