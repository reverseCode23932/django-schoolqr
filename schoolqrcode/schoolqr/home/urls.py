from django.urls import path
from .views import homepage, delete_item

urlpatterns = [
    path('', homepage),
    path('delete/<int:id>/', delete_item),
]
