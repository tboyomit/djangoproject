# accounts/urls.py

from django.urls import path                    # new to line \\
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]