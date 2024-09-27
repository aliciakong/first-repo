#define URL route for index() view
from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
]