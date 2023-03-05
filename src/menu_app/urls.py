from django.urls import path
from .views import MenuItemView

app_name = 'menu_app'

urlpatterns = [
    path('<str:menu_slug>/', MenuItemView.as_view(), name='menu')
]