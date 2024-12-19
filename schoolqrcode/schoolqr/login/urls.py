from django.urls import path
from .views import get_form, success, remove

urlpatterns = [
    path('', get_form),
    path('<int:id>/', success),
    path('delete_this/<int:id>/', remove)
]
