#admin1/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('staff',listCategory),
    path('create_category',createCategory ,name='create-category') ,
    path('update_category/<pk>',updateCategory,name='update-category'),
    path('delete_category/<pk>',deleteCategory ,name='delete-category'),

    path('list_product',listProduct,name='list-product'),
    path('create_product',createProduct,name='create-product'),
    path('update_product/<pk>',updateProduct ,name='update-product'),
    path('delete_product/<pk>',deleteProduct,name='delete-product'),

    path('list_order',listOrder),
    path('view_order/<pk>',viewOrder),
    path('confirm_order/<pk>',confirmOrder),
    path('cancel_order/<pk>',cancelOrder),

    path('information_user/<pk>',informationUer),
]