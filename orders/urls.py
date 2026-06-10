from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.dashboard,    name='dashboard'),
    path('orders/',                 views.order_list,   name='order_list'),
    path('orders/add/',             views.order_add,    name='order_add'),
    path('orders/edit/<int:pk>/',   views.order_edit,   name='order_edit'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('orders/export/',          views.export_csv,   name='export_csv'),
    path('orders/import/', views.import_excel, name='import_excel'),
    path('orders/delete-all/', views.delete_all_orders, name='delete_all_orders'),
]