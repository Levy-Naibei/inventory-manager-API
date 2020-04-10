from django.urls import path, include
from . import views

urlpatterns = [
    path('products', views.product_list.as_view()),
    path('products/<int:pk>', views.product_detail.as_view()),
    path('categories/', views.category_list.as_view()),
    path('categories/<int:pk>', views.category_detail.as_view()),
    path('locations/', views.location_list.as_view()),
    path('locations/<int:pk>', views.location_detail.as_view()),
    path('transactions/', views.transaction_list.as_view()),
    path('transactions/<int:pk>', views.transaction_detail.as_view()),
]
