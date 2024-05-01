from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.get_product_data, name='get_product_data'),
]
